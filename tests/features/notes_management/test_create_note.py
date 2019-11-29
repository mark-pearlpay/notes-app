import requests

from http import HTTPStatus
from pytest_bdd import scenario, given, when, then
import pytest

from handler.note import handler_create_note


@pytest.fixture(scope='module')
def global_data():
    return {'response': {}}


@scenario('../../../features/notes_management.feature', 'Create a note')
def test_scenario_impl():
    pass


@when("I create a new note")
def step_impl(global_data):
    payload = {
        "title": "test title",
        "content": "test content"
    }

    # TODO: Destruct me to api_path, host and full_api_path
    full_api_path = "http://localhost:3000/notes"
    # full_api_path = "https://y8cfunmkll.execute-api.ap-southeast-1.amazonaws.com/Prod/notes"

    try:
        global_data['response'] = requests.post(full_api_path, json=payload)
    except Exception as e:
        raise e

    assert global_data['response'].json() != {}


@then("response should be successful")
def step_impl(global_data):
    assert global_data['response'].status_code == HTTPStatus.CREATED.value