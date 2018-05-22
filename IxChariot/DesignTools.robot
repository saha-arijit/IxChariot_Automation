*** Settings ***
Library           ../IxChariot_Libraries/CreateTestCase.py

*** Test Cases ***
Create Flows
    [Setup]
    Arguments    Flow Group    Test Case Name    EndPoint 1    EndPoint 2    Direction    Protocol
    ...    Script    Duration (secs)    Radio_UID_1    Channel_UID_1    Radio_UID_2    Channel_UID_2
    ...    Radio_UID_3    Channel_UID_3    Radio_UID_4    Channel_UID_4    Radio_UID_5    Channel_UID_5
    ...    Create    Number of users
    CreateTestCase    MAC    Bell_MAC1    DESKTOP    MAC1    DS    TCP
    ...    TCP High Performance    10    1    1,2,3    2    36,40,44
    ...    \    \    \    \    \    ${EMPTY}
    ...    \    6
    CreateTestCase    MAC    Bell_MAC1    MAC1    DESKTOP    US    TCP
    ...    TCP High Performance    10    1    1,2,3    ${EMPTY}    ${EMPTY}
    ...    \    \    \    \    ${EMPTY}    ${EMPTY}
    ...    \    6
    CreateTestCase    MAC    Bell_MAC2    DESKTOP    MAC2    DS    TCP
    ...    TCP High Performance    10    1    1,2,3    2    36,40,44
    ...    \    \    \    \    \    ${EMPTY}
    ...    \    6
    CreateTestCase    MAC    Bell_MAC2    MAC2    DESKTOP    US    TCP
    ...    TCP High Performance    10    1    1,2,3    2    36
    ...    \    \    \    \    ${EMPTY}    ${EMPTY}
    ...    \    6
    [Teardown]    Refresh
