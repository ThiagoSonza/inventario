import os, sys

def MemoryLnx():
    # comando puro:
    # dmidecode -t 17 | awk 'BEGIN { FS=":"; OFS="\t" } /Size|Locator|Type:|Speed|Manufacturer|Serial Number|Part Number/ { gsub(/^[ \t]+/,"",$2); line = (line ? line OFS : "") $2 } /^$/ { print line; line="" }' | grep -iv "no module"

    a = "dmidecode -t 17 | awk '"
    b = 'BEGIN { FS=":"; OFS="\t" } /Size|Locator|Type:|Speed|Manufacturer|Serial Number|Part Number/ { gsub(/^[ \t]+/,"",$2); line = (line ? line OFS : "") $2 } /^$/ { print line; line="" }'
    c = "' | grep -iv "
    d = '"no module"'
    command = '' . join(a + b + c + d)
    resultado =  os.popen(command).read()
    memorycard = []

    for x in resultado.split("\n")[1:-1]:
        x = x.replace("MB", "").replace(" ", "")

        mem = []

        for y in x.split("\t"):
            mem.append(y)

        memorycard.append([ mem[0], mem[1], mem[5], mem[3], mem[7], mem[6], ''. join(mem[4] + ' - ' + mem[8]) ])

    return memorycard


def MemoryWin():

    memorycard = []
    process    = os.popen('wmic memorychip get capacity, devicelocator, Manufacturer, memorytype, partnumber, serialnumber, speed')
    result     = process.read()
    process.close()    
        
    for m in result.split("  \n")[1:-1]:
        m = m.replace("\n", "")
        
        mem = []
        
        for n in m.split(" "):
            if len(n) > 1 :
                mem.append(n)
        
        memorycard.append(mem)
    
    return memorycard

def cardMemory():
    if "win" in sys.platform.lower():
        memoryChip = MemoryWin()
    else:
        memoryChip = MemoryLnx()

    return memoryChip