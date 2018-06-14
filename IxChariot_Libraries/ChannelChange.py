import paramiko, sys
import time
import logger


def hubChannel(radio, channelValue):
	flagTry = 0
	try :
		host = "192.168.2.1" 	# 192.168.2.1
		username = "admin" 		# admin
		password = "admin"		# admin

		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host, username=username, password=password)
		
		channel = ssh.invoke_shell()
		channel.send('login root\n') # entering usename = root
		while not channel.recv_ready():
		    time.sleep(2)
		channel.recv(1024)
		channel.send('root\n') # password for root username
		while not channel.recv_ready():
		    time.sleep(2)
		channel.recv(1024)
		try:
			statusFlg = checkChannel(channel, radio, channelValue)
		except:
			logger.ErrorLog ("Error occured in Channel Change.")
			raise Exception
	except:
		print Exception

	return statusFlg

def checkChannel(channel, radio, channelValue):

	statusFlg = False
	logger.MessageLog ("Starting to check current channel.")

	channel.send('xmo-client -p Device/WiFi/Radios/Radio[@uid=\''+ radio +'\']/Channel\n')  #command checks currnt channel
	while not channel.recv_ready():
	    time.sleep(2)
	output = channel.recv(1024)
	# logger.MessageLog(output)
	time.sleep(2)
	output = output.split("\n")
	# logger.MessageLog (output)

	for outputLines in output:
		if "value" in outputLines:
			outputLines = outputLines.split(": ")
			outValue = outputLines[1].replace("'","")
			logger.MessageLog ("Current Channel is: " + outValue.rstrip() + " for Radio:" + radio)

			if int(channelValue) == int(outValue): # checks whether current channel matches the channel value entered by user and returns True on success
				logger.MessageLog ("Entered value is the current channel.")
				statusFlg = True
			else:
				logger.MessageLog ("Need to change the current channel value to " + channelValue)
				statusFlg = changeNCheck(channel, radio, channelValue)
				try:
					if not statusFlg:
						logger.MessageLog ("Second Try")
						statusFlg = changeNCheck(channel, radio, channelValue)
						if not statusFlg:
							logger.MessageLog ("Third try")
							statusFlg = changeNCheck(channel, radio, channelValue)
							if not statusFlg:
								logger.ErrorLog ("Error occured in changing channel value.")
				except NameError:
					logger.ErrorLog ("Error occured in channel change.")
					raise Exception

		if "XMO_UNKNOWN_PATH_ERR" in outputLines:
			logger.ErrorLog ("Could not find valid Radio with entered value : "+radio +".")
			statusFlg = False

	return statusFlg

def changeNCheck(channel, radio, channelValue):
	statusFlg = False

	channel.send('xmo-client -p Device/WiFi/Radios/Radio[@uid=\''+ radio +'\']/Channel -s '+ channelValue+'\n')
	while not channel.recv_ready():
	    time.sleep(2)
	output = channel.recv(1024)
	# logger.MessageLog(output)
	time.sleep(2)
	output = output.split("\n")
	# logger.MessageLog (output)

	channel.send('xmo-client -p Device/WiFi/Radios/Radio[@uid=\''+ radio +'\']/Channel\n')  #command checks currnt channel
	while not channel.recv_ready():
	    time.sleep(2)
	output = channel.recv(1024).split("\n")
	# logger.MessageLog(output)

	for outputLines in output:
		if "value" in outputLines:
			outputLines = outputLines.split(": ")
			outValue = outputLines[1].replace("'","")
			logger.MessageLog ("Current Channel is: " + outValue.rstrip() + " for Radio: " + radio)

			if int(channelValue) == int(outValue): # checks whether current channel matches the channel value entered by user and returns True on success
				logger.MessageLog ("Channel value successfully changed.")
				statusFlg = True
			else:
				statusFlg = False

		elif "error" in outputLines:
			statusFlg = False

	return statusFlg
