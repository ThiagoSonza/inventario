import psutil

def hardDisks():
    drps        = psutil.disk_partitions()
    drives      = [dp.mountpoint for dp in drps if dp.fstype in ('NTFS','EXT4')]
    partitions  = []

    for drive in drives:
        usage     = psutil.disk_usage(drive)
        particao  = drive.replace('\\', '').replace(':', '')
        total     = (usage.total // 2**30)
        utilizado = (usage.used // 2**30)
        livre     = (usage.free // 2**30)
        
        partitions.append([particao, total, utilizado, livre])

    return partitions