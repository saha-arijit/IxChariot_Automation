import time
import sys
import logger
def TestCase_validation(global_FlowGroup,global_TestCaseName,global_EndPoint1,global_EndPoint2,global_Direction,global_Protocol,Script,Duration,Create,NumberOfUsers,dict): 
	
	
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

		
		
	if global_Direction == 'DS' or global_Direction == 'US':
		logger.MessageLog ("Parameters for Direction has been validated successfully.")
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

	return 1	

	
		
		
		
	
		
	
	
		