from pupil_tracker import eye_tracker

from time import time

listOfImages = ['centro.jpeg','izquierda.jpeg','prueba.jpeg', 'prueba2.jpg', 'prueba3.jpeg']
#listOfImages = ['ejemplo.jpeg']
def test():
    myET = eye_tracker(1)
    for i in range(0, len(listOfImages)*40-1):
        for image in listOfImages:
            x,y=myET.pupilDetect('./Images/' +image)
            
            if(x != None and y != None):
                myET.decodify(x,y)
          #      print('px , py , angle , force ',myET.decodify(x,y))
print(len(listOfImages)*40)
start = time()
test()
end = time()
x = end - start
print('exec time: ', x)