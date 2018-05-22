import time
import sys
import logger, re
def TestCase_validation(global_FlowGroup,global_TestCaseName,global_EndPoint1,global_EndPoint2,global_Direction,global_Protocol,Script,Duration,Radio1, Channel1, Radio2, Channel2,Radio3, Channel3,\
								Radio4,Channel4,Radio5,Channel5,Create,NumberOfUsers,dict): 
	
	
	ScriptList = ['TCP High Performance','TCP Low Performance', 'TCP Small Packets Performance', 'TCP Baseline Performance', 'TCP Small Packets Performance', \
					'UDP Low Performance', 'UDP Baseline Performance', 'UDP High Performance']


	logger.MessageLog("Starting Test Parameter Validation of Test Case : %s " %global_TestCaseName+'_'+global_Direction)

	if (len(global_FlowGroup)<=0):
		flag = 0
		logger.ErrorLog ("FlowGroup cannot be left blank.")
		return flag
	else:
		logger.MessageLog ("Parameters for FlowGroup has been validated successfully.") 
				
	
	if (len(global_TestCaseName)<=0):
		flag = 0
		logger.ErrorLog ("TestCaseName cannot be left blank.")
		return flag
	else:
		logger.MessageLog ("Parameters for TestCaseName has been validated successfully.")
		
		
	if global_EndPoint1 == global_EndPoint2 :
		flag = 0
		logger.ErrorLog ("Entered EndPoint1 and EndPoint2 values cannot be the same.")
		return flag		
	else:
		pass
		
	if global_EndPoint1 in dict or global_EndPoint1.lower() in dict:
		logger.MessageLog ("Parameters for EndPoint1 has been validated successfully.")
	elif (len(global_EndPoint1) <= 0):
		flag = 0
		logger.ErrorLog ("EndPoint1 value cannot be left blank.")
		return flag
	else:
		flag = 0
		logger.ErrorLog ("Entered EndPoint1 value   %s  is not present in userconfig file." %global_EndPoint1)
		return flag
	
	
	if global_EndPoint2 in dict or global_EndPoint2.lower() in dict:
		logger.MessageLog ("Parameters for EndPoint2 has been validated successfully.")
	elif (len(global_EndPoint2) <= 0):
		flag = 0
		logger.ErrorLog ("EndPoint2 value cannot be left blank.")
		return flag
	else:
		flag = 0
		logger.ErrorLog ("Entered EndPoint2 value   %s  is not present in usercofig file." %global_EndPoint2)
		return flag

		
		
	if global_Direction == 'DS' and global_EndPoint1 == "DESKTOP":
		logger.MessageLog ("Parameters for Direction has been validated successfully.")
	elif global_Direction == 'US' and global_EndPoint2 == "DESKTOP":
		logger.MessageLog ("Parameters for Direction has been validated successfully.")
	elif global_Direction == 'DS' and global_EndPoint1 != "DESKTOP" or global_Direction == 'US' and global_EndPoint2 != "DESKTOP":
		floag = 0
		logger.ErrorLog ("Direction value does not have accurate EndPoint value.")
		return flag
	elif (len(global_Direction) <= 0):
		flag = 0
		logger.ErrorLog ("Direction value cannot be left blank.")
		return flag
	else:
		flag = 0
		logger.ErrorLog ("Direction value entered is invalid. Choose either \"DS\" or \"US\".")
		return flag	
		
		
	if global_Protocol == 'TCP' or global_Protocol == 'UDP':
		logger.MessageLog ("Parameters for Protocol has been validated successfully.")
	elif (len(global_Protocol) <= 0):
		flag = 0
		logger.ErrorLog ("Protocol value cannot be left blank.")
		return flag
	else:
		flag = 0
		logger.ErrorLog ("Entered Protocol value   %s  is not a valid entry." %global_Protocol)
		return flag

	
	if Script in ScriptList:
		logger.MessageLog ("Parameters for Script has been validated successfully.")
	elif (len(Script)<=0):
		flag = 0
		logger.ErrorLog ("Script Name cannot be left blank.")
		return flag
	else:
		flag = 0
		logger.ErrorLog ("Entered Script value   %s  is not a valid entry." %Script)
		return flag
		
		
	Duration = int(Duration)
	
	if type(Duration) is int:	
		logger.MessageLog ("Parameters for Duration has been validated successfully.")
		
	elif (len(Duration) <= 0):
		flag = 0
		logger.MessageLog ("Duration field cannot be left blank.")
		return flag
	else:
		flag = 0
		logger.ErrorLog ("Entered Duration value is not a valid entry %s" %Duration)
		return flag
	
	NumberOfUsers = int(NumberOfUsers)
	
	if (NumberOfUsers <= 10):
		pass
	elif (len(NumberOfUsers) <= 0):
		flag = 0
		logger.ErrorLog ('Number of users cannot be left blank.')
		return flag
	else:
		flag = 0
		logger.ErrorLog ('The current license does not support more than 10 users.')
		return flag
	
	if type(NumberOfUsers) is int:
		logger.MessageLog ("Parameters for NumberOfUsers has been validated successfully.")
	
	else:
		flag = 0
		logger.ErrorLog ("Entered NumberOfUsers value  %s  is not a valid entry." %NumberOfUsers)
		return flag
		

	# Checks for comma separated integer values for Channel
	if len(Channel1) > 1:
		for char in Channel1:
			if not char.isdigit() and char not in [" ", ","]:
				logger.ErrorLog ("Channel 1 should have numeric values separated by comma.")
				return 0

	if len(Channel2) > 1:
		for char in Channel2:
			if not char.isdigit() and char not in [" ", ","]:
				logger.ErrorLog ("Channel 2 should have numeric values separated by comma.")
				return 0

	if len(Channel3) > 1:
		for char in Channel3:
			if not char.isdigit() and char not in [" ", ","]:
				logger.ErrorLog ("Channel 3 should have numeric values separated by comma.")
				return 0

	if len(Channel4) > 1:
		for char in Channel4:
			if not char.isdigit() and char not in [" ", ","]:
				logger.ErrorLog ("Channel 4 should have numeric values separated by comma.")
				return 0

	if len(Channel5) > 1:
		for char in Channel5:
			if not char.isdigit() and char not in [" ", ","]:
				logger.ErrorLog ("Channel 5 should have numeric values separated by comma.")
				return 0

	if not Radio1.isdigit() and len(Radio1) > 0:
		logger.ErrorLog ("Radio 1 accepts numeric values only.")
		return 0
	elif not Radio2.isdigit()and len(Radio2) > 0:
		logger.ErrorLog ("Radio 2 accepts numeric values only.")
		return 0
	elif not Radio3.isdigit()and len(Radio3) > 0:
		logger.ErrorLog ("Radio 3 accepts numeric values only.")
		return 0
	elif not Radio4.isdigit()and len(Radio4) > 0:
		logger.ErrorLog ("Radio 4 accepts numeric values only.")
		return 0
	elif not Radio5.isdigit()and len(Radio5) > 0:
		logger.ErrorLog ("Radio 5 accepts numeric values only.")
		return 0		
		
	if (len(Radio1) <= 0) and (len(Channel1) != 0):
		flag = 0
		logger.ErrorLog ('Radio1 field cannot be left blank if Channel1 is not blank.')
		return flag	
	elif (len(Radio2) <= 0) and (len(Channel2) != 0):
		flag = 0
		logger.ErrorLog ('Radio2 field cannot be left blank if Channel2 is not blank.')
		return flag
	elif (len(Radio3) <= 0) and (len(Channel3) != 0):
		flag = 0
		logger.ErrorLog ('Radio3 field cannot be left blank if Channel3 is not blank.')
		return flag	
	elif (len(Radio4) <= 0) and (len(Channel4) != 0):
		flag = 0
		logger.ErrorLog ('Radio4 field cannot be left blank if Channel4 is not blank.')
		return flag
	elif (len(Radio5) <= 0) and (len(Channel5) != 0):
		flag = 0
		logger.ErrorLog ('Radio5 field cannot be left blank if Channel5 is not blank.')
		return flag
		
		
	if (len(Radio1) != 0) and (len(Channel1) <= 0): 
		flag = 0
		logger.ErrorLog ('Channel1 field cannot be left blank if Radio1 is not blank.')
		return flag
	elif(len(Radio2) != 0) and (len(Channel2) <= 0): 
		flag = 0
		logger.ErrorLog ('Channel2 field cannot be left blank if Radio2 is not blank.')
		return flag
	elif(len(Radio3) != 0) and (len(Channel3) <= 0):
		flag = 0
		logger.ErrorLog ('Channel3 field cannot be left blank if Radio3 is not blank.')
		return flag
	elif(len(Radio4) != 0) and (len(Channel4) <= 0):
		flag = 0
		logger.ErrorLog ('Channel4 field cannot be left blank if Radio4 is not blank.')
		return flag
	elif(len(Radio5) != 0) and (len(Channel5) <= 0):
		flag = 0
		logger.ErrorLog ('Channel5 field cannot be left blank if Radio5 is not blank.')
		return flag
		
		
	if (((len(Radio1) != 0) and (len(Channel1) != 0))  or ((len(Radio1) <= 0) and (len(Channel1) <= 0))):
		logger.MessageLog('Parameters for Radio1 and channel1 has been validated successfully.')
	elif (((len(Radio2) != 0) and (len(Channel2) != 0))  or ((len(Radio2) <= 0) and (len(Channel2) <= 0))):
		logger.MessageLog('Parameters for Radio2 and channel2 has been validated successfully.')
	elif (((len(Radio3) != 0) and (len(Channel3) != 0))  or ((len(Radio3) <= 0) and (len(Channel3) <= 0))):
		logger.MessageLog('Parameters for Radio3 and channel3 has been validated successfully.')
	elif (((len(Radio4) != 0) and (len(Channel4) != 0))  or ((len(Radio4) <= 0) and (len(Channel4) <= 0))):
		logger.MessageLog('Parameters for Radio4 and channel4 has been validated successfully.')
	elif (((len(Radio5) != 0) and (len(Channel5) != 0))  or ((len(Radio5) <= 0) and (len(Channel5) <= 0))):
		logger.MessageLog('Parameters for Radio5 and channel5 has been validated successfully.')

	
	return 1	

	
		
		
		
	
		
	
	
		