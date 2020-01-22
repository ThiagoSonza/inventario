import subprocess, re

def query_wmic(properties, device_id=None):
	query = ['WMIC PATH Win32_VideoController']

	if device_id:
		query.append('WHERE "DeviceID LIKE \'{}\'"'.format(device_id))

	query.append('GET {}'.format(properties))

	process = subprocess.Popen(' '.join(query), stdout=subprocess.PIPE)
	output = process.stdout.read().decode().replace('\r\r', '')
	rows = []

	for line in output.splitlines()[1:-1]:
		rows.append(re.sub('\s\s+', '\n', line).splitlines())
	return rows

class GPU():
	def __init__(self, total_memory, device_id, name):
		self.name = name
		# It is important to note that due to the limitations of 32-bit integers, Windows will not report
		# the correct memory for any GPU with a total memory greater than 4GB.
		self.total_memory = int(int(total_memory) / 1048576)
		self.device_id = device_id

def get_gpus():
	rows = query_wmic('AdapterRAM,DeviceID,Name')
	gpus = []

	for row in rows:
		gpus.append(GPU(*row))

	return gpus

def placaVideo():
	gpus = []
			
	for gpu in get_gpus():
		name 	= gpu.name
		memoria = gpu.total_memory
		
		gpus.append([name, memoria])
		
	return gpus