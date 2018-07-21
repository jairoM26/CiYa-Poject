from pupil_tracker import eye_tracker

listOfImages = ['centro.jpeg','derecha.jpeg','izquierda.jpeg','prueba.jpeg', 
                'prueba2.jpg', 'prueba3.jpeg','pruebaWB.png']

def test():
    myET = eye_tracker(1)
    for image in listOfImages:
        x,y=myET.pupilDetect('./Images/' +image)
        
        if(x != None and y != None):
            print('px , py , angle , force ',myET.decodify(x,y))
test()