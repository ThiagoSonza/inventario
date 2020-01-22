import socket, re, uuid

def ipAddr():
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    ips  = []

    for addr in addrs:        
        ips.append( addr[4][0] )
    
    return ips