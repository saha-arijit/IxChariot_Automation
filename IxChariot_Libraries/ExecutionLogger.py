import os, sys
from robot.api.deco import keyword

drive = os.path.splitdrive(sys.executable)
sys.path.append(drive[0] + '\IxChariot_Automation\IxChariot_Libraries')
import logger
logger.LoggerMethod(__name__)

@keyword('Arguments')
def comment(*message):
	pass
