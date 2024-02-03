from django.db.models.fields.json import KeyTextTransform

class NestableKeyTextTransform:
    def __new__(cls, field, *path):
        if not path:
            raise ValueError("Path must contain at least one key.")
        head, *tail = path
        field = KeyTextTransform(head, field)
        for head in tail:
            field = KeyTextTransform(head, field)
        return field