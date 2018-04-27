from ixia.webapi import *
import ixchariotApi
import time
import os, sys
sys.path.append('C:/IxChariot_Automation/IxChariot_Libraries')
import ZipFile
import configFile
import logger

def Run_BELL_MAC3_DS():
	dict_config = configFile.userconfig()
	webServerAddress = "https://192.168.2.30"
	apiVersion = "v1"
	username = "cage.noire@gmail.com"
	password = "Atl12345"
	apiKey = "7faf1207-b2ff-4a90-9a70-ea5ec87040f1"
	filePath = "..\IxChariot_ExecutionReport\\" + dict_config["HHUB_Version"] + "\\MAC\DS\DESKTOP\\"
	fileName = "MAC3_TCP High Performance"+ '_' +time.strftime("%Y%m%d-%H%M%S",time.localtime())

	CreatefilePath = filePath + fileName
	if not os.path.exists(filePath):
		os.makedirs(filePath)

	logger.MessageLog("Connecting to %s" %webServerAddress)
	api = webApi.connect(webServerAddress, apiVersion, None, username, password)
	session = api.createSession("ixchariot")
	logger.MessageLog ("Created session %s" % session.sessionId)

	logger.MessageLog ("Starting the session...")
	session.startSession()
	logger.MessageLog("Session has Started.")
	logger.MessageLog ("Configuring the test...")

	testOptions = session.httpGet("config/ixchariot/testOptions")
	testOptions.testDuration = 10
	testOptions.consoleManagementQoS = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, "Best Effort")
	testOptions.endpointManagementQoS = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, "Best Effort")
	session.httpPut("config/ixchariot/testOptions", data = testOptions)

	src_EndpointsList = ["192.168.2.29/192.168.2.29"]
	dst_EndpointsList = ["192.168.2.102/192.168.2.102"]

	name = "MAC"
	direction = "SRC_TO_DEST"
	topology = "FULL_MESH"
	flowgroup = ixchariotApi.createFlowGroup(name, direction, topology)
	session.httpPost("config/ixchariot/flowGroups", data = flowgroup)

	for src_Endpoint in src_EndpointsList:
		ips = src_Endpoint.split('/')
		session.httpPost("config/ixchariot/flowGroups/1/network/sourceEndpoints", data = ixchariotApi.createEndpoint(ips[0], ips[1]))

	for dst_Endpoint in dst_EndpointsList:
		ips = dst_Endpoint.split('/')
		session.httpPost("config/ixchariot/flowGroups/1/network/destinationEndpoints", data = ixchariotApi.createEndpoint(ips[0], ips[1]))

	flowList = [
					[ "TCP High Performance" , 6 , "TCP" ,"None","None"]
				]

	for i in range (0, len(flowList)):
		flowData = flowList[i]
		flowName = flowData[0]
		users = flowData[1]
		protocol = flowData[2]
		sourceQoSName = flowData[3]
		destinationQoSName = flowData[4]
		flowScript = ixchariotApi.getFlowScriptFromResourcesLibrary(session, flowName)

		sourceQoSTemplate = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, sourceQoSName)
		destinationQoSTemplate = ixchariotApi.getQoSTemplateFromResourcesLibrary(session, destinationQoSName)

		flow = ixchariotApi.createFlow(flowScript, users, protocol, sourceQoSTemplate, destinationQoSTemplate)
		session.httpPost("config/ixchariot/flowGroups/1/settings/flows", data = flow)

	try:
		logger.MessageLog ("Starting the test...")
		result = session.runTest()

		logger.MessageLog ("The test ended")

		results = api.getTestResults(1)

		resultId = results.testRunInformationList[0].testRunId

		stream = api.httpPost('results/%d/report' % resultId)

		logger.MessageLog("Saving the test results into PDF files")
		with open(CreatefilePath +'.pdf', 'wb') as file:
			file.write(stream.encode('utf-8'))

		logger.MessageLog ("Saving the test results into zipped CSV files...\n")
		with open(CreatefilePath + '.zip', 'wb+') as statsFile:
			api.getStatsCsvZipToFile(result.testId, statsFile)

	except Exception, e:
		logger.ErrorLog ("Error in test case execution.")

	logger.MessageLog ("Stopping the session...")
	session.stopSession()

	logger.MessageLog ("Deleting the session...")
	session.httpDelete()

	ZipFile.UnZipFile(CreatefilePath)

