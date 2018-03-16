import socket
import pytz
import datetime

def getDateTimeZ():
    country = raw_input("Add country")
    zone = raw_input("Add Zone")
    tz = zone+'/'+country
    hourCountry = pytz.timezone(tz)
    hourCountry.zone
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    fmt = '%Y-%m-%d %H:%M:%S '
    print (now.astimezone(hourCountry)).strftime(fmt)

def getHostName():
    hostName = socket.gethostname()
    return hostName

def getHostIp():
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    return ipAddress