import sys, platform, socket
from _insere import getPC, saveData
from hw import getDevice
from harddisks import hardDisks
from ipaddresses import ipAddr
from memory import cardMemory 

softwares  = None
placavideo = None
cardMem    = None

# get ID pc inventoried
idDevice  = getPC(socket.gethostname())

# list device
device    = getDevice()

# list of partitions and harddisks
hardDisks = hardDisks()

# list of IPs 
ipAddr    = ipAddr()

# list of memories
cardMem   = cardMemory()

# Softwares, GPU, Memory
if "win" in sys.platform.lower():
    from softwares import Software
    from videocard import placaVideo 
    
    # list of programs installed
    softwares = Software()
    
    # list of videocards installed in device
    placavideo = placaVideo()
    
# faz a chamada da função insere para gravar os dados no banco
saveData(idDevice, device, ipAddr, cardMem, hardDisks, softwares, placavideo)