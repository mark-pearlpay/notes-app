import json
import uuid

from http import HTTPStatus

from util import log

from model.note import Note

logger = log.setup_custom_logger(__name__)


def handler_create_note(event, context):
    # TODO: pass payload to service
    # TODO: validation should be in service
    bodydict = json.loads(event['body'])

    # TODO: move me in repository code
    note = Note(hash_key=str(uuid.uuid4()), **bodydict)
    note.save()
    note.refresh()

    # TODO: use existing wrappers and helpers
    return {
        "body": json.dumps(dict(note)),
        "statusCode": HTTPStatus.CREATED
    }
