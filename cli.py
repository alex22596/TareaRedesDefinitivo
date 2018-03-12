# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2013. 8. 5.
@author: kangstar
'''

from socket import *
import thread, time


def recvMsg(sock):
    while True:
        recvmsg = sock.recv(1024)
        print
        '<Server>>> ' + recvmsg


if __name__ == '__main__':
    host = raw_input('HOST(default:localhost): ')
    port = raw_input('PORT(default:8008): ')

    host = host if (len(host) > 0) else 'localhost'
    port = int(port) if (len(port) > 0) else 8008

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))

        thread.start_new_thread(recvMsg, (s,))

        time.sleep(1)
        nickmsg = raw_input('My Nickname: ')
        s.send(nickmsg)

        time.sleep(2)
        print
        'Wait!...'

        while True:
            sendmsg = raw_input(' - Send: ')
            if sendmsg == 'exit()':
                break
            s.send(sendmsg)

        s.close()
    except:
        print
        'Wrong address!'

    raw_input('Exit client (Press any key!)')