from pupil_tracker import eye_tracker
import picamera
from threading import Thread
import threading
from time import sleep
from os import system

global listOfImages, flagTakePicture, myET, camera
listOfImages = []
flagTakePicture = True
myET = eye_tracker(1)
myET.videoTest()

camera = None

def startCamera():
    try:
        camera = picamera.PiCamera()
        camera.resolution = (800,600)
    except:
        print("Error abriendo la camara")

def takeAPictureThread(pImageName = "imageTest"):
    global listOfImages, camera
    i = 0
    while flagTakePicture:
        #if (i == 5): break
        pict = pImageName + str(i) + ".jpeg"
	try:
	    camera.start_preview()	    
	    camera.capture(pict)
	    camera.stop_preview()
	except:
	    print("Error tomando foto")
	    break
        listOfImages.append(pict)
        i +=1
	sleep(0.3)

def processPicture():
    global listOfImages
    i = 0
    while True:
        #if(i==5): break
        if (listOfImages != []):
            pict = listOfImages[0]
            print(myET.pupilDetect(pict))
            listOfImages.remove(pict)
            i+=1
            system("rm " + pict)
	    sleep(0.3)

'''
a = Thread(target=takeAPictureThread, args=())
a.start()
b = Thread(target=processPicture, args=())
b.start()
'''