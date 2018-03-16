import os

def getProcess():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    cont = 0
    for pid in pids:
        try:
            cont += 1
            print open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
        except IOError:  # proc has already terminated
            continue
    print 'Number of Process: ', cont
