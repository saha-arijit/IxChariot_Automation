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
		file.write("\t"+ "Arguments\t" + "Radio1\t" + "Channel1\t"+ "Radio2\t" + "Channel2\t"+ "Radio3\t" + "Channel3\t"+ "Radio4\t" + "Channel4\t"+ "Radio5\t" + "Channel5\t" + "\n")
		file.close()

	for i in flowGroupList:
		for j in fileNameList:
			res = j.split(',')
			k = 0
			list1 = []
			while (k != len(res)):
				if res[k] == '#':
					list1.append(k)
				k = k + 1
			if (res[1] == i):
				for item in robotFileList:
					if res[1]+'.robot' in item:
						#									radio1           *channel1                  **    *RADIO2         **   *channel2                 **    *radio3          **   *channel3                 **   
						fileWriting(item,res[0],res[1],res[(list1[0]) + 1] , res[(list1[0]) + 2 : list1[1]] , res[(list1[1]) + 1], res[(list1[1]) + 2 :list1[2]] , res[(list1[2]) + 1] , res[(list1[2]) + 2 :list1[3]], \
						#               *radio4           *  *channel4                  **   *radio5          **   *channel5        **
						                 res[(list1[3]) + 1], res[(list1[3]) + 2 : list1[4]] , res[(list1[4]) + 1] , res[(list1[4]) + 2 :])

def fileWriting(fileName,content,flowGroup,radio1,channel1,radio2,channel2,radio3,channel3,radio4,channel4,radio5,channel5):

	file = open (fileName, "r") # this is for appending new data to existing file
	lines = file.readlines()
	index = 0
	presentFlag = 0

	channel1 = ",".join(channel1)
	channel2 = ",".join(channel2)	
	channel3 = ",".join(channel3)
	channel4 = ",".join(channel4)
	channel5 = ",".join(channel5)
	
	if len(radio1) == 0 and len(channel1) == 0:
		channel1 = "\\"
		radio1 = "\\"
	if len(radio2) == 0 and len(channel2) == 0:
		channel2 = "\\"
		radio2 = "\\"
	if len(radio3) == 0 and len(channel3) == 0:	
		channel3 = "\\"
		radio3 = "\\"
	if len(radio4) == 0 and len(channel4) == 0:	
		channel4 = "\\"
		radio4 = "\\"
	if len(radio5) == 0 and len(channel5) == 0:	
		channel5 = "\\"
		radio5 = "\\"

	for line in lines:
		index += 1

		if 'Test Cases' in line:
			TC = index
			
		if "Settings" in line:
			sett = index
			
		if 'RunAllFlows' in line:
			RA = index
	
	libraryContent = '../IxChariot_FlowScripts/'+flowGroup+'/'+content+'.py'
	lines.insert(RA+2,"\t" +'Run_'+content+ "\t"+ radio1 + "\t" + channel1+ "\t"+ radio2 + "\t" + channel2+"\t" + radio3 + "\t" + channel3+ "\t"+ radio4 + "\t" + channel4+"\t" + radio5 + "\t" + channel5 + "\n"+'\n')
	lines.insert(sett ,"Library           "+libraryContent+"\n")
	lines.insert(TC+1,content +"\n" )
	lines.insert(TC+2 ,"\t"+ "Arguments\t" + "Radio1\t" + "Channel1\t"+ "Radio2\t" + "Channel2\t"+ "Radio3\t" + "Channel3\t"+ "Radio4\t" + "Channel4\t"+ "Radio5\t" + "Channel5\t" + "\n" + \
					"\t" +'Run_'+content+ "\t"+ radio1 + "\t" + channel1+ "\t"+ radio2 + "\t" + channel2+"\t" + radio3 + "\t" + channel3+ "\t"+ radio4 + "\t" + channel4 +"\t" + radio5 + "\t" + channel5 + "\n"+'\n')

	file = open (fileName , 'w')
	lines = "".join(lines)
	file.write(lines)
	file.close()

