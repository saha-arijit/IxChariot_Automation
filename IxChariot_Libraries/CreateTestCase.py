import os
import time
import sys
import CreateRobotFile
import Validation
import logger
import subprocess

from robot.api.deco import keyword

@keyword('Arguments')
def comment(*message):
	pass
	loggerTest = logger.LoggerMethod(__name__)

global fileNameList, flowGroupList, existList

fileNameList = []
flowGroupList = []
existList = ['userconfig.txt','DesignTools.robot']
	
def userconfig():
	global dict_config
	dict_config = {}
	ConfigFilePath = 'userconfig.txt'
	configfile = open(ConfigFilePath,'r')
	x = configfile.read()
	lines = x.split("\n")
	
	for line in lines:
		
		if '$' in line:
			start = line.index('{')
			end = line.index('}')
			newstr = line[start+1:end]
			key = newstr.strip()
			
			start1 = line.index('}')
			end1 = line.index('#')
			newstr1 = line[start1+1:end1]
			value = newstr1.strip()
			
			dict_config[key] = value
			
def CreateTestCase(FlowGroup,TestCaseName,EndPoint1,EndPoint2,Direction,Protocol,Script,Duration,Create,NumberOfUsers):
	global global_TestCaseName , global_Direction,global_FlowGroup,global_Protocol , reopenFlag
	global_TestCaseName = TestCaseName.upper()
	global_Direction = Direction.upper()
	global_FlowGroup = FlowGroup.upper()
	global_Protocol = Protocol.upper()
	global_EndPoint1 = EndPoint1.upper()
	global_EndPoint2 = EndPoint2.upper()
	reopenFlag = 0
	# userconfig()

	try: 
		userconfig()
		# reopenFlag = 1
	except NameError:
		# reopenFlag = 0
		logger.ErrorLog('Error happend in userconfig file')
		raise NameError
		Refresh()
	
	if(len(Create)<=0) or Create.upper() == 'YES':
		createFlag = "yes"
		logger.MessageLog("Creating test case file for " + global_TestCaseName + "_" + global_Direction)
	else:
		createFlag = "no"
		logger.MessageLog("Not creating test case file for " + global_TestCaseName + "_" + global_Direction)

		
	# Creation of TestFlow files
	if createFlag == "yes":
	
		# Validation of the entered parameters
		logger.MessageLog("Starting validation of Test Parameters.")

		reopenFlag = Validation.TestCase_validation(global_FlowGroup,global_TestCaseName,global_EndPoint1,global_EndPoint2,global_Direction,global_Protocol,Script, \
												Duration,Create,NumberOfUsers,dict_config)

		if reopenFlag == 1:
			logger.MessageLog("Validation of Test Parameters completed successfully.")
		elif reopenFlag == 0:
			logger.ErrorLog("Validation of test parameters NOT completed successfully.")
			raise ValueError
		
		logger.MessageLog("Starting writing to python file.")
		
		FilePath = '..\\IxChariot_FlowScripts\\' + global_FlowGroup + '\\'
		fileName = global_TestCaseName + '_' + global_Direction
		
		PDFfilePath = '..\\IxChariot_ExecutionReport\\' + global_FlowGroup + "\\"+ global_Direction + "\\" + global_EndPoint1 + "\\\\"
		PDFFileName =  global_EndPoint2 + "_" + Script

		if not os.path.exists(FilePath):
			os.makedirs(FilePath)

		file = open(FilePath + fileName +'.py', 'w')
		
		file.write('from ixia.webapi import *' +'\n')
		file.write('import ixchariotApi'+'\n')
		file.write('import time'+'\n')
		file.write('import os' + "\n")
		file.write('import logger' + '\n'+'\n')

		
		file.write('def Run_'+global_TestCaseName+ '_' + global_Direction + '():' +'\n')
		
		file.write('\t'+'webServerAddress = "'+ dict_config['var_webServerAddress'] +'"' +'\n')
		file.write('\t'+'apiVersion = "'+ dict_config['var_ixcapiVersion'] +'"' +'\n')
		file.write('\t'+'username = "'+ dict_config['var_ixcusername'] +'"' +'\n')
		file.write('\t'+'password = "'+ dict_config['var_ixcpassword'] +'"' +'\n')
		file.write('\t'+'apiKey = "'+ dict_config['var_ixcapikey'] +'"'+'\n')
		file.write('\t'+'filePath = "'+ PDFfilePath + '"'+'\n')
		file.write('\t'+'fileName = "'+ PDFFileName + '\"'+ "+ '_' +"  + 'time.strftime("%Y%m%d-%H%M%S",time.localtime())' + '\n'+'\n')
		file.write('\t'+'CreatefilePath = filePath + fileName'+'\n')
		
		file.write('\t'+'if not os.path.exists(filePath):'+'\n')
		file.write('\t'+'\t'+'os.makedirs(filePath)'+'\n'+'\n')
				
		file.write('\t'+'logger.MessageLog("Connecting to %s" %webServerAddress)'+'\n')
		file.write('\t'+'api = webApi.connect(webServerAddress, apiVersion, None, username, password)'+'\n')
		file.write('\t'+'session = api.createSession("ixchariot")'+'\n')
		file.write('\t'+'logger.MessageLog ("Created session %s" % session.sessionId)'+'\n'+'\n')
		
		file.write('\t'+'logger.MessageLog ("Starting the session...")'+'\n')
		
		file.write('\t'+'session.startSession()'+'\n')
		file.write('\t'+'logger.MessageLog("Session has Started.")'+'\n')
		file.write('\t'+'logger.MessageLog ("Configuring the test...")'+'\n'+'\n')
		
		file.write('\t'+'testOptions = session.httpGet("config/ixchariot/testOptions")'+'\n')
		file.write('\t'+'testOptions.testDuration = ' + Duration +'\n')
		file.write('\t'+'testOptions.consoleManagementQoS = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, "Best Effort")'+'\n')
		file.write('\t'+'testOptions.endpointManagementQoS = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, "Best Effort")'+'\n')
		file.write('\t'+'session.httpPut("config/ixchariot/testOptions", data = testOptions)'+'\n'+'\n')

		try:
			file.write('\t'+'src_EndpointsList = ["'+ dict_config[global_EndPoint1] +'/'+ dict_config[global_EndPoint1] +'"]'+'\n')
		except KeyError:
			file.write('\t'+'src_EndpointsList = ["'+ dict_config[global_EndPoint1.lower()] +'/'+ dict_config[global_EndPoint1.lower()] +'"]'+'\n')

		try:
			file.write('\t'+'dst_EndpointsList = ["'+ dict_config[global_EndPoint2] +'/'+ dict_config[global_EndPoint2] +'"]'+'\n'+'\n')
		except:
			file.write('\t'+'dst_EndpointsList = ["'+ dict_config[global_EndPoint2.lower()] +'/'+ dict_config[global_EndPoint2.lower()] +'"]'+'\n'+'\n')

		file.write('\t'+'name = \"'+ global_FlowGroup+'\"' +'\n')
		file.write('\t'+'direction = "SRC_TO_DEST"' +'\n')
		file.write('\t'+'topology = "FULL_MESH"' + '\n')
		file.write('\t'+'flowgroup = ixchariotApi.createFlowGroup(name, direction, topology)'+'\n')
		file.write('\t'+'session.httpPost("config/ixchariot/flowGroups", data = flowgroup)'+'\n'+'\n')
		
		file.write('\t'+'for src_Endpoint in src_EndpointsList:'+'\n')
		file.write('\t'+'\t'+"ips = src_Endpoint.split('/')"+'\n')
		file.write('\t'+'\t'+'session.httpPost("config/ixchariot/flowGroups/1/network/sourceEndpoints", data = ixchariotApi.createEndpoint(ips[0], ips[1]))'+'\n'+'\n')
		
		file.write('\t'+'for dst_Endpoint in dst_EndpointsList:'+'\n')
		file.write('\t'+'\t'+"ips = dst_Endpoint.split('/')"+'\n')
		file.write('\t'+'\t'+ 'session.httpPost("config/ixchariot/flowGroups/1/network/destinationEndpoints", data = ixchariotApi.createEndpoint(ips[0], ips[1]))' +'\n'+'\n')
		
		file.write('\t'+'flowList = ['+'\n')
		file.write('\t'+'\t'+'\t'+'\t'+'\t'+ '[ "'+ Script + '" , ' + NumberOfUsers + ' , "'+ global_Protocol+'" ,'+  \
															'"None","None"]'+'\n'+'\t'+'\t'+'\t'+'\t'+']'+'\n'+'\n')
		
		file.write('\t'+'for i in range (0, len(flowList)):'+'\n')
		file.write('\t'+'\t'+'flowData = flowList[i]'+'\n')
		file.write('\t'+'\t'+'flowName = flowData[0]'+'\n')
		file.write('\t'+'\t'+'users = flowData[1]'+'\n')
		file.write('\t'+'\t'+'protocol = flowData[2]'+'\n')
		file.write('\t'+'\t'+'sourceQoSName = flowData[3]'+'\n')
		file.write('\t'+'\t'+'destinationQoSName = flowData[4]'+'\n')
		file.write('\t'+'\t'+'flowScript = ixchariotApi.getFlowScriptFromResourcesLibrary(session, flowName)'+'\n'+'\n')
		
		file.write('\t'+'\t'+'sourceQoSTemplate = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, sourceQoSName)'+'\n')
		file.write('\t'+'\t'+'destinationQoSTemplate = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, destinationQoSName)'+'\n'+'\n')
		file.write('\t'+'\t'+'flow = ixchariotApi.createFlow(flowScript, users, protocol, sourceQoSTemplate, destinationQoSTemplate)'+'\n')
		file.write('\t'+'\t'+'session.httpPost("config/ixchariot/flowGroups/1/settings/flows", data = flow)'+'\n'+'\n')
		
		file.write('\t'+'try:'+'\n')
		file.write('\t'+'\t'+'logger.MessageLog ("Starting the test...")'+'\n')
		file.write('\t'+'\t'+'result = session.runTest()'+'\n'+'\n')
		
		file.write('\t'+'\t'+'logger.MessageLog ("The test ended")'+'\n'+'\n')
		
		file.write('\t'+'\t'+'results = api.getTestResults(1)'+'\n'+'\n')
		
		file.write('\t'+'\t'+'resultId = results.testRunInformationList[0].testRunId'+'\n'+'\n')
		
		file.write('\t'+'\t'+"stream = api.httpPost('results/%d/report' % resultId)"+'\n'+'\n')
		
		file.write('\t'+'\t'+'logger.MessageLog("Saving the test results into PDF files")'+'\n')
		file.write('\t'+'\t'+"with open(CreatefilePath +'.pdf', 'wb') as file:"+'\n')
		file.write('\t'+'\t'+'\t'+'file.write(stream.encode(\'utf-8\'))'+'\n'+'\n')
		
		
		file.write('\t'+'\t'+'logger.MessageLog ("Saving the test results into zipped CSV files...\\n")'+'\n')
		file.write('\t'+'\t'+"with open(CreatefilePath + '.zip', 'wb+') as statsFile:"+'\n')
		file.write('\t'+'\t'+'\t'+'api.getStatsCsvZipToFile(result.testId, statsFile)'+'\n'+'\n')
		
		file.write('\t'+'except Exception, e:'+'\n')
		
		file.write('\t'+'\t'+'logger.ErrorLog ("Error in test case execution.")'+'\n'+'\n')
		
		file.write('\t'+'logger.MessageLog ("Stopping the session...")'+'\n')
		file.write('\t'+'session.stopSession()'+'\n'+'\n')
		
		file.write('\t'+'logger.MessageLog ("Deleting the session...")'+'\n')
		file.write('\t'+'session.httpDelete()'+'\n')
		
		logger.MessageLog("Successfully created test case python file.")
				
		file.close()

	if fileName+','+global_FlowGroup in fileNameList:
		pass
	else:
		fileNameList.append(fileName+','+global_FlowGroup)
	if global_FlowGroup in flowGroupList:
		pass
	else:
		flowGroupList.append(global_FlowGroup)

	existList.append('Execute_Flow_' + global_FlowGroup + '.robot')
	
def Refresh():

	global reopenFlag

	try:
		if reopenFlag == 1:
			logger.MessageLog("Start creating robot file.")
			try:
				CreateRobotFile.CreateRobotFile(global_TestCaseName,global_Direction,global_FlowGroup,fileNameList,flowGroupList)
				logger.MessageLog("Successfully created test case robot file.")
			except:
				logger.ErrorLog("Error occured in creation of robot file for flowgroup.")
				# reopenFlag = 0
				raise Exception

			removableFiles = []
			
			drive = os.path.splitdrive(sys.executable)

			listdir = os.listdir(drive[0]+"\\IxChariot_Automation\\IxChariot\\")
			for item in listdir:
				if item in existList:
					pass
				else:
					removableFiles.append(item)
			for file  in removableFiles:
				os.remove(file)

			# Enter condition for no rows filled by user in CreateTest
			try:
				if reopenFlag == 1:
					logger.MessageLog ("Refreshing RIDE.")
					task   = 'tasklist /v /fo csv | findstr /i "python.exe"'
					result = subprocess.check_output(task, shell=True)
					result = result.split(',')
					res    = result[1].split('"')
					kill   = 'taskkill /F /PID '+res[1]
					os.system(kill)
					time.sleep(5)
					os.system('start '+drive[0]+'\\IxChariot_Automation\\tools\\openRIDE.vbs')
			except NameError:
				logger.ErrorLog ("Atleast one row entry required for execution process.")
				raise Exception
	except NameError:
		logger.ErrorLog ("Atleast one row entry required for execution process.")
		raise Exception

 