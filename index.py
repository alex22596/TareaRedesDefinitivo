import socket
def getHostName():
    hostName = socket.gethostname()
    return hostName

def getHostIp():
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    return ipAddress