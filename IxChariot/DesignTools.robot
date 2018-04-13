*** Settings ***
Library           ../IxChariot_Libraries/CreateTestCase.py

*** Test Cases ***
Create Flows
    [Setup]
    Arguments    Flow Group    Test Case Name    EndPoint 1    EndPoint 2    Direction    Protocol
    ...    Script    Duration (secs)    Create    Number of users
    CreateTestCase    MAC    Bell_MAC1    DESKTOP    MAC1    DS    TCP
    ...    TCP High Performance    10    \    2
    CreateTestCase    MAC    Bell_MAC1    MAC1    DESKTOP    US    UDP
    ...    UDP Low Performance    10    \    1
    Comment    CreateTestCase    ANDRIOD    Bell_MAC2    DESKTOP    MAC1    DS
    ...    TCP    TCP High Performance    10    \    5
    Comment    CreateTestCase    ANDRIOD    Bell_MAC2    MAC2    DESKTOP    US
    ...    UDP    UDP Low Performance    10    \    5
    [Teardown]    Refresh
