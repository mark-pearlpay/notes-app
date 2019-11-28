import requests

from http import HTTPStatus
from pytest_bdd import scenario, given, when, then

from handler.note import handler_create_note


response = {}


@scenario('../../../features/notes_management.feature', 'Create a note')
def test_scenario_impl():
    pass


@when("I create a new note")
def step_impl():
    payload = {
        "title": "test title",
        "content": "test content"
    }

    # TODO: Destruct me to api_path, host and full_api_path
    full_api_path = "http://localhost:3000/notes"

    try:
        test_response = requests.post(full_api_path, data=payload)
    except Exception as e:
        raise e

    assert test_response != {}


@then("response should be successful")
def step_impl():
    assert response['statusCode'] == HTTPStatus.CREATED