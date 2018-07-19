'''
 * file: server.py
 * base on Albert Huang <albert@csail.mit.edu> code from pybluez examples
 *
 * @brief programa servidor de bluetooth
 *
 * @details se utiliza un servidor con puerto rfcomm para conectarse por bluetooth
 *
 *
 * @author LuisDiego Delgado Alfaro <>
 * @author JuanDiego Delgado Vargas <>
 * @author JeanCarlos Gonzales Hernandez <>
 * @author Mariana Guerrero Jimenez <>
 * @author Jairo Mendez Martinez <jairomendezmartinez@gmail.com>
 * @date 19-07-2018
'''

from bluetooth import *
from Convert import *

def startServer(port = 1):
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen()

    #uuid de la maquina
    uuid = "bcb9605d-55f6-4081-b267-eaa91f610a9c"

    advertise_service( server_sock, "BluetoothServer",
                    service_id = uuid,
                    service_classes = [ uuid, SERIAL_PORT_CLASS ],
                    profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )
                    
    print "Waiting for connection on RFCOMM channel %d" % port

    client_sock, client_info = server_sock.accept()
    print "Accepted connection from ", client_info

    try:
        while True:
            data = client_sock.recv(1024)
            if len(data) == 0: print('no data recieved')
            print(len(data))
    except IOError:
        print 'error'
        print "disconnected"

    client_sock.close()
    print "all done"
