from pupil_tracker import eye_tracker

from time import time

listOfImages = ['1.jpg','2.jpg','3.jpg', '4.jpg', '5.jpg']
#listOfImages = ['ejemplo.jpeg']
def test():
    myET = eye_tracker(1)
    #for i in range(0, len(listOfImages)*40-1):
    for image in listOfImages:
        x,y=myET.pupilDetect('./Images/' +image)
        
        if(x != None and y != None):
            print('image ', image, 'x , y, px , py , angle , force ',x,y,myET.decodify(x,y))
#                myET.decodify(x,y)
                
test()