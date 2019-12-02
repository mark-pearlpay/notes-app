import os

import pytest
from pytest_bdd import scenario, given, when, then


from model.note import Note


@given("note table exists")
def step_impl():
    # pass
    if not Note.exists():
        Note.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

    return Note.exists()


@pytest.fixture(scope='module')
def global_data():
    return {'response': {}}