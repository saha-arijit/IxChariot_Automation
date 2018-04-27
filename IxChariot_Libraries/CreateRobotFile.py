import os 
import sys
import logger
import time


def CreateRobotFile(global_TestCaseName,global_Direction,global_FlowGroup,fileNameList,flowGroupList):
	global robotFileList
	robotFileList = []

	for i in flowGroupList:
		robotFileList.append('..\IxChariot\\'+ 'Execute_Flow_' +i+ '.robot')

	for i in robotFileList:
		file = open(i,'w')
		file.write ("*** Settings ***" + "\n")
		file.write ("Library           "+ '../IxChariot_Libraries/ExecutionLogger.py'+"\n")
		file.write ("\n"+"*** Test Cases ***" + "\n")
		file.write('RunAllFlows'+'\n')
		file.close()

	for i in flowGroupList:
		for j in fileNameList:
			res = j.split(',')
			if (res[1] == i):
				for item in robotFileList:
					if res[1]+'.robot' in item:
						fileWriting(item,res[0],res[1])

def fileWriting(fileName,content,flowGroup):

	# file = open(fileName,'a')
	# file.write(content)
	# file.write('\n')
	file = open (fileName, "r") # this is for appending new data to existing file
	lines = file.readlines()
	index = 0
	presentFlag = 0
	
	for line in lines:
		index += 1

		if 'Test Cases' in line:
			TC = index
			
		if "Settings" in line:
			sett = index
			
		if 'RunAllFlows' in line:
			RA = index
	# print fileName
	# print content
	libraryContent = '../IxChariot_FlowScripts/'+flowGroup+'/'+content+'.py'
	lines.insert(RA+1,"\t"+ 'Run_'+content+ "\n")
	lines.insert(sett ,"Library           "+libraryContent+"\n")
	lines.insert(TC+1,content +"\n" )
	lines.insert(TC+2 ,"\t"+ 'Run_'+content+ "\n"+'\n')

	file = open (fileName , 'w')
	lines = "".join(lines)
	file.write(lines)
	file.close()

