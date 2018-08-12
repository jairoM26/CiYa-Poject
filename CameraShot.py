
import picamera
import time

def test():
    camera = picamera.PiCamera()

    camera.resolution = (800, 600)

    camera.start_preview()

    #cd Citime.sleep(1)

    camera.capture("snapshot.jpg", resize=(640, 480))

    camera.stop_preview()

test()
