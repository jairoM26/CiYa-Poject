from pupil_tracker import *
from decodification import *

listOfImages = ['centro.jpeg','derecha.jpeg','izquierda.jpeg']

def test():
    for image in listOfImages:
        px, py = pupilDetect(image)
        print(decodeCoords(px,py))
    
test()