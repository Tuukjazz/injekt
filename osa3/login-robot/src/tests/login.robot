*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
	Create User  peee  pe123121212121212
	Input Credentials  peee  pe12341212121

Login With Nonexistent Username
	Input Credentials  peeee  1233

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
