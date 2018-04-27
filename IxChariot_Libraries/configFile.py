import sys
def userconfig():
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

	return dict_config