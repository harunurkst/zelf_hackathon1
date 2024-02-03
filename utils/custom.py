from django.db.models.fields.json import KeyTextTransform


class NestableKeyTextTransform:
    """
    Custom class to use Nested key JSONField aggregation
    """
    def __new__(cls, field, *path):
        if not path:
            raise ValueError("Path must contain at least one key.")
        head, *tail = path
        field = KeyTextTransform(head, field)
        for head in tail:
            field = KeyTextTransform(head, field)
        return field