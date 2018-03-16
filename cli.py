from socket import *
import thread
import time
import index
import processLinux


def recvMsg(sock):
    while True:
        recvmsg = sock.recv(1024)
        print
        '<Server>>> ' + recvmsg


def levantarCliente():
    host = raw_input('Server IP: ')
    port = raw_input('Server Port: ')

    host = host if (len(host) > 0) else ' '
    port = int(port) if (len(port) > 0) else ' '

    if host == ' ' or port == ' ':
        print 'IP or Port invalid'
        mainMenu()

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))

        thread.start_new_thread(recvMsg, (s,))

        time.sleep(1)
        nickmsg = raw_input('My nickname: ')
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
        'Wrong addres!'
    raw_input('Bye Client (press a key!)')

def mainMenu():
    while True:
        option = int(input(" 1. Get client name   \n"
                              " 2. Get client IP     \n"
                              " 3. Get time from another country        \n"
                              " 4. Get number of processes running on the server \n"
                              " 5. Send message client - server         \n"
                              " 6. Exit     \n"
                              "     Option: "))
        if option == 1:
            print("Server Name: ", index.getHostName())
        elif option ==2:
            print("Server IP: ", index.getHostIp())
        elif option == 3:
            index.getDateTimeZ()
        elif option == 4:
            optionProcess = int(input("1. Windows\n"
                  "2. Linux\n"
                  "     Option: "))
            if optionProcess == 1:
                print()
            elif optionProcess == 2:
                processLinux.getProcess()
        elif option == 5:
            levantarCliente()
        elif option == 6:
            break

if __name__ == '__main__':
    mainMenu()