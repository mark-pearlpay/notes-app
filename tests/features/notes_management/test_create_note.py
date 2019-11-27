from pytest_bdd import scenario, given, when, then


@scenario('../../../features/notes_management.feature', 'Create a note')
def test_scenario_impl():
    pass


@when("I create a new note")
def step_impl():
    pass
    # raise NotImplementedError(u'STEP: When I create a new note')


@then("response should be successful")
def step_impl():
    pass
    # raise NotImplementedError(u'STEP: Then response should be successful')