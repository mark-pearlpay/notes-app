import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Note(Model):
    class Meta:
        table_name = 'Note'
        host = ('http://' + os.environ.get('LOCALSTACK-HOSTNAME') + ':4569') if os.environ.get(
            'LOCALSTACK-HOSTNAME') != 'none' else None

    note_id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(null=True)
    content = UnicodeAttribute(null=True)
