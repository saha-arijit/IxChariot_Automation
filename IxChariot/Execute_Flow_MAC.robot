*** Settings ***
Library           ../IxChariot_FlowScripts/MAC/BELL_MAC1_US.py
Library           ../IxChariot_FlowScripts/MAC/BELL_MAC1_DS.py

*** Test Cases ***
BELL_MAC1_US
	Run_BELL_MAC1_US

BELL_MAC1_DS
	Run_BELL_MAC1_DS

RunAllFlows
	BELL_MAC1_DS
	BELL_MAC1_US
