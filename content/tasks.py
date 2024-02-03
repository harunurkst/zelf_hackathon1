import time

import requests
from content.models import Content, Author
from main.celery import app


# TODO: Store API KEY in .env file
api_key = '67c2f809sk_ac38sk_4dcbsk_8837sk_c5a6614ef48c1706933134'


def get_author(unique_id):
    """
    Get author data from third party using his unique_id
    :param unique_id:
    :return:
    """
    # TODO: Store url in .env file
    url = 'https://hackapi.hellozelf.com/backend/api/v1/authors/'+str(unique_id)
    headers = {
        'x-api-key': api_key
    }
    resp = requests.get(url, headers=headers)
    if resp.ok:
        return resp.json()
    return None


def get_content(page_number):
    """
    A funtion to get content data from third party API page by page
    :param page_number:
    :return:
    """
    headers = {
        'x-api-key': api_key
    }
    url = 'https://hackapi.hellozelf.com/backend/api/v1/contents?page=' + str(page_number)
    response = requests.get(url, headers=headers)

    if response.ok:
        resp_data = response.json()
        next_id = resp_data['next']  # Next page number
        content_data = resp_data['data']
        for data in content_data:
            content_unique_id = data['unique_id']
            author = data.get('author', None)
            if author:
                author_id = author['id']

                # IF author not exist in DB, create new object
                author, created = Author.objects.get_or_create(unique_id=author_id, username=author['username'])
                # If author not exist in DB, get author Detail from API and save to DB
                if created:
                    author_obj = get_author(author_id)
                    if author_obj:
                        author_data = author_obj.get('data', None)
                        if author_data:
                            # collecting single element as all author data looks same,
                            # This may change as business logic
                            author.data = author_data[0]
                            author.save()

            content, is_created = Content.objects.get_or_create(unique_id=content_unique_id, defaults={'author': author})
            # If content not exist in DB
            if is_created:
                print("New content created..")
                content.data = data
                content.save()
            else:
                # check content data JSON is same as DB content data JSON. Check Full JSON is not perfect, we should
                # check randomly changeable data field
                if not content.data == data:
                    print("content data updated..")
                    content.data = data
                    content.save()
                else:
                    print("content data not updated. continue..")
                    continue
        return next_id
    else:
        json_resp = response.json()
        if json_resp['code'] == 401:
            # Request limit exceeded, sleep some time
            print("Request limit exceeded, sleep some time")
            time.sleep(5)
            return get_content(page_number)
        elif json_resp['code'] == 419 or json_resp['code'] == 402:
            # Something went wrong, try again
            print("Something went wrong, try again")
            return get_content(page_number)
        else:
            return get_content(page_number)

@app.task
def collect_contents():
    """
    Celery task to collect data from Third party API
    :return:
    """
    next_page_number = 1
    # collect data until next page not None
    while next_page_number:
        next_page_number = get_content(next_page_number)
        print("next page", next_page_number)


