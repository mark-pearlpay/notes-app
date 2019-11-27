Feature: Notes Management
    As a user
    I should be able to manage my notes

Background:
    Given note table exists

Scenario: Create a note
    When I create a new note
    Then response should be successful

#Scenario: Get a note
#    When I get an existing note
#    Then response should be successful
#
#Scenario: Update a note
#    When I update an existing note
#    Then response should be successful
#
#Scenario: Delete a note
#    Given an existing note
#    And I delete that note
#    Then response should be successful
#
#Scenario: List all notes
#    Given notes exist
#    When I list all notes
#    Then response should be successful