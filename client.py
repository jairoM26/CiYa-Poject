'''
 * file: client.py
 * base on Albert Huang <albert@csail.mit.edu> code from pybluez examples
 *
 * @brief programa cliente de bluetooth
 *
 * @details se utiliza un cliente con puerto rfcomm para conectarse por bluetooth
 *
 *
 * @author LuisDiego Delgado Alfaro <>
 * @author JuanDiego Delgado Vargas <>
 * @author JeanCarlos Gonzales Hernandez <>
 * @author Mariana Guerrero Jimenez <>
 * @author Jairo Mendez Martinez <jairomendezmartinez@gmail.com>
 * @date 19-07-2018
'''

from bluetooth import discover_devices, find_service, BluetoothSocket, RFCOMM
import sys
import time
#import picamera
from Convert import convertImageToString

global addr, service_matches
addr = None
service_matches = None

uuid = "bcb9605d-55f6-4081-b267-eaa91f610a9c"

'''
'''
def searchServer(deviceBluetoothName):
    global addr
    nearby_devices = discover_devices(lookup_names = True)    

    for device in nearby_devices:
        if(device[1] == deviceBluetoothName):
            print(device)
            addr = device[0]


'''
'''
def clientConnect(pUuid, pAddr=addr, port =1):
    
    print('searching')
    while(True):
        service_matches = find_service( uuid = pUuid, address = pAddr )

        if len(service_matches) != 1:
            print('device found')
            break
    
    try:
        first_match = service_matches[0]    
        name = first_match["name"]
        host = first_match["host"]

        print "connecting to \"%s\" on %s" % (name, host)

        # Create the client socket
        sock=BluetoothSocket( RFCOMM )
        sock.connect((host, port))
        return sock
    except:
        print('connection refuse')
    
'''
'''
def sendData():
    searchServer('jairo')
    try:
        sock = clientConnect(uuid)
        while(True):           
            for i in range(0,4):
                imageName = 'pict'+str(i)+'.jpeg'
                #takeAPicture(imageName)
                strPict = convertImageToString(imageName)
                time.sleep(1)
                sock.send(strPict)                
    except:
        sock.close()
        print('Cant send image')
    

'''

def takeAPicture(pImageName):
    camera = picamera.Picamera()
    camera.resolution = (800,600)
    camera.start_preview()
    camera.capture(pImageName, resize =(200,200))
    camera.stop_preview()
'''


