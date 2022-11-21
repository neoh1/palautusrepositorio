*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kekkonen  k3kk15pr3ss4
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username too short; less than 3 letters

Register With Valid Username And Too Short Password
    Input Credentials  nalle  passu1
    Output Should Contain  Password should be 8 characters or more

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nalle  salasana
    Output Should Contain  Password has to have non-letter characters


*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command  
