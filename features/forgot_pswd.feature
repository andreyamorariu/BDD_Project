Feature: Jules forgot_password tests

    Background:
      #se ruleaza inainte de fiecare test, se pun in general given-urile
      Given signin: I am a user on Jules signin page

    @jules
    Scenario: Wrong email validation message
      When signin: I click on forgot_password_link
      When forgot_password: I set my email "abcd"
      Then forgot_password: I verify that email validation message is correct

    @jules
    Scenario Outline: Wrong email validation message with table data
      When signin: I click on forgot_password_link
      When forgot_password: I set my email "<email>"
      Then forgot_password: I verify that email validation message is correct

      Examples:
        | email     |
        | abcde@com |
        | fghth@com |