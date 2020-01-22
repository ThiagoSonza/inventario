import platform, socket, cpuinfo, os, sys, re, uuid, psutil, psycopg2, multiprocessing

os_type = sys.platform.lower()

def Manufacturer():
    if "win" in sys.platform.lower():
        import wmi
        c = wmi.WMI ()
        systeminfo = c.Win32_ComputerSystem()[0]
        return systeminfo.Manufacturer
    elif "linux" in os_type: 
        command = "cat /sys/class/dmi/id/board_vendor"
        return os.popen(command).read().replace("\n","").replace("  ","").replace(" ","")

def Model():
    if "win" in sys.platform.lower():
        import wmi
        c = wmi.WMI ()
        systeminfo = c.Win32_ComputerSystem()[0]
        return systeminfo.Model
    elif "linux" in os_type:
        command = "cat /sys/class/dmi/id/product_name"
        return os.popen(command).read().replace("\n","").replace("  ","").replace(" ","")

def Serial():
    if "win" in os_type:
        command = "wmic bios get serialnumber"
        a = os.popen(command).read().replace("\n","")
        b = a.split(" ")
        return b[2]
         
    elif "linux" in os_type:
        command = "sudo cat /sys/class/dmi/id/product_serial"
        return os.popen(command).read().replace("\n","").replace("  ","").replace(" ","")

def getDevice():
    device      = []

    fabricante  = Manufacturer()
    modelo      = Model()
    serial      = Serial()
    name        = socket.gethostname()
    macaddress  = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
    processador = '' . join( cpuinfo.get_cpu_info()['brand'] +  ' (' + str(multiprocessing.cpu_count()) + ' Cores)')
    system      = '' . join(platform.system() + ' ' + platform.release() + ' ' + platform.machine() + ' ' + platform.version())
    lastlogin   = os.getlogin()

    device.extend( [fabricante, modelo, serial, name, macaddress, processador, system, lastlogin ] )

    return device