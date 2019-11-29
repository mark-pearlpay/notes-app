import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute

dynamo_host = os.environ.get('HOST', 'none')


class Note(Model):
    class Meta:
        table_name = 'Note'
        region = 'ap-southeast-1'
        host = ('http://' + dynamo_host + ':4569') if dynamo_host != 'none' else None

    note_id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(null=True)
    content = UnicodeAttribute(null=True)

    def __iter__(self):
        for name, attr in self.get_attributes().items():
            if isinstance(attr, ListAttribute):
                attribute_list = []
                for item in getattr(self, name):
                    attribute_list.append(item.serialize_map(item))
                yield name, attribute_list
            else:
                yield name, attr.serialize(getattr(self, name))
