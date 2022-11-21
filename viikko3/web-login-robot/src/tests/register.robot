*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  asdf
    Set Password  asdf1234
    Set Password Confirmation  asdf1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username   ab
    Set Password   asdf1234
    Set Password Confirmation  asdf1234
    Submit Credentials
    Register Should Fail With Message  Username too short; less than 3 letters

Register With Valid Username And Too Short Password
    Set Username   asdf
    Set Password   as12
    Set Password Confirmation  as12
    Submit Credentials
    Register Should Fail With Message  Password should be 8 characters or more


Register With Nonmatching Password And Password Confirmation
    Set Username  asdf
    Set Password  asdf1234
    Set Password Confirmation  asdf123r
    Submit Credentials
    Register Should Fail With Message  Passwords do not match


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
