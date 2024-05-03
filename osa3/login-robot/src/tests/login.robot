*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
	Create User  pe  pe123
	Input Credentials  pe  pe1234

Login With Nonexistent Username
	Input Credentials  pee  1233

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
