*** Settings ***
Library           ../IxChariot_FlowScripts/MAC/BELL_MAC3_US.py
Library           ../IxChariot_FlowScripts/MAC/BELL_MAC3_DS.py
Library           ../IxChariot_Libraries/ExecutionLogger.py

*** Test Cases ***
BELL_MAC3_US
	Run_BELL_MAC3_US

BELL_MAC3_DS
	Run_BELL_MAC3_DS

RunAllFlows
	Run_BELL_MAC3_DS
	Run_BELL_MAC3_US
