from socket import *
import thread, time
import index

def recvMsg(sock):
    while True:
        recvmsg = sock.recv(1024)
        print
        '<Server>>> ' + recvmsg

def levantarCliente():
    host = raw_input('IP del servidor: ')
    port = raw_input('Puerto del servidor: ')

    host = host if (len(host) > 0) else ' '
    port = int(port) if (len(port) > 0) else ' '
    if host == ' ' or port == ' ':
        print 'Ingrese una IP o un puerto valido'
        mainMenu()
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))

        thread.start_new_thread(recvMsg, (s,))

        time.sleep(1)
        nickmsg = raw_input('Mi nombre: ')
        s.send(nickmsg)

        time.sleep(2)
        print
        'Wait!...'

        while True:
            sendmsg = raw_input(' - Enviar: ')
            if sendmsg == 'exit()':
                break
            s.send(sendmsg)

        s.close()
    except:
        print
        'Direccion incorrecta!'
    raw_input('Cliente Saliendo (Presione una tecla!)')

def mainMenu():
    print(".::Welcome to CHATEC::.")
    while True:
        option = int(input(" 1. Get server name   \n"
                              " 2. Get server IP     \n"
                              " 3. Get quantity of running processes    \n"
                              " 4. Get time from another country        \n"
                              " 5. Send message client - server         \n"
                              " 6. Exit     \n"
                              "     Option: "))
        if option == 1:
            print("Server Name: ",index.getHostName())
        elif option ==2:
            print("Server IP: ", index.getHostIp())
        elif option == 3:
            print("")
        elif option == 4:
            getDateTimeZ("")
            print("")
        elif option == 5:
            levantarCliente()
        elif option == 6:
            break

if __name__ == '__main__':
    mainMenu()