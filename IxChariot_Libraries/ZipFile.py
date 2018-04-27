import os
import sys
import zipfile
from zipfile import *


def UnZipFile(CreatefilePath):

	folder, fileName = os.path.split(CreatefilePath)
	
	zip = zipfile.ZipFile(CreatefilePath + ".zip")
	zip.extractall(CreatefilePath)
	zip.close()

	zip = zipfile.ZipFile(CreatefilePath + ".zip")
	zip.extract('ixchariot.csv', folder)
	zip.close()

	prevname = folder + "\\" + 'ixchariot.csv'
	newname = folder + "\\" + fileName + '.csv'
	os.rename(prevname , newname)
	
	os.remove(folder + "\\" + fileName + ".zip")

