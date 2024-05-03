*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  pep  pep12312312
	Output Should Contain  New user registered
	
Register With Already Taken Username And Valid Password
	Input Credentials  kalle  kalle123456
	Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
	Input Credentials  es  kalle123456
	Output Should Contain  Username is too short
	
Register With Enough Long But Invalid Username And Valid Password
	Input Credentials  es!!  kalle123456
	Output Should Contain  Username should only contain letters a-z

Register With Valid Username And Too Short Password
	Input Credentials  esee  a1
	Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
	Input Credentials  esee  kaaaaaaaaaaaaa
	Output Should Contain  Password should contain letters a-z and numbers
	
*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command