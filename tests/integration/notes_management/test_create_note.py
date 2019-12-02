import requests
import json

from http import HTTPStatus
from pytest_bdd import scenario, given, when, then

from handler.note import handler_create_note


@scenario('../../../features/notes_management.feature', 'Create a note')
def test_scenario_impl():
    pass


@when("I create a new note")
def step_impl(global_data):
    event = {
        "body": json.dumps({
            "title": "test title",
            "content": "test content"
        })
    }

    try:
        response = handler_create_note(event, {})

        global_data['response'] = requests.Response()
        global_data['response'].status_code = response['statusCode']

        def json_func():
            return response['body']
        global_data['response'].json = json_func
    except Exception as e:
        raise e

    assert global_data['response'].json() != {}


@then("response should be successful")
def step_impl(global_data):
    assert global_data['response'].status_code == HTTPStatus.CREATED.value