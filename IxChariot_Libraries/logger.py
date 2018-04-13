import logging
import time 
import sys
import os
from logging.handlers import TimedRotatingFileHandler
import inspect	

def LoggerMethod(message):

	log_file_name = "..//IxChariot_Results//"+'DetailedLog'+time.strftime("%Y%m%d",time.localtime())+".log"
	logging_level = logging.INFO
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %I:%M:%S %p')
	handler = TimedRotatingFileHandler(log_file_name,when="midnight")
	handler.setFormatter(formatter)
	logger = logging.getLogger()
	logger.addHandler(handler) 
	logger.setLevel(logging.INFO)

	
def MessageLog(message):

    func = inspect.currentframe().f_back.f_code
    filename = func.co_filename.split('\\')
    logging.info("%s -> %s :: %s" % (filename[len(filename)-1],func.co_name,message))
	
def ErrorLog(message):

    func = inspect.currentframe().f_back.f_code
    filename = func.co_filename.split('\\')
 
    logging.error("%s -> %s :: %s" % (filename[len(filename)-1],func.co_name,message ))



