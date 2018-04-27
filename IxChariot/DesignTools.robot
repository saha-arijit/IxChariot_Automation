*** Settings ***
Library           ../IxChariot_Libraries/CreateTestCase.py

*** Test Cases ***
Create Flows
    [Setup]
    Arguments    Flow Group    Test Case Name    EndPoint 1    EndPoint 2    Direction    Protocol
    ...    Script    Duration (secs)    Create    Number of users
    CreateTestCase    MAC    Bell_MAC3    DESKTOP    MAC3    DS    TCP
    ...    TCP High Performance    10    \    6
    CreateTestCase    MAC    Bell_MAC3    MAC3    DESKTOP    US    TCP
    ...    TCP High Performance    10    \    6
    [Teardown]    Refresh
