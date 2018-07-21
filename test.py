from pupil_tracker import eye_tracker

listOfImages = ['centro.jpeg','derecha.jpeg','izquierda.jpeg','prueba.jpeg', 
                'prueba2.jpg', 'prueba3.jpeg','pruebaWB.png']

def test():
    myET = eye_tracker(0)
    for image in listOfImages:
        print(myET.pupilDetect('./Images/' +image))
test()