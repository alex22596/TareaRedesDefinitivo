import os
import psutil


def getProcess():
    listProcess = []
    cantProcess = 0
    for process in psutil.process_iter():
        listProcess.append(process)
        #print process
    cantProcess = len(listProcess)
    print 'Number of Process: ', cantProcess

