from Tkinter import * ##Interfaz
import time ##Hora de la computadora
from threading import Thread ##Thread (hilo), para evitar threading.Thread
import random ##Metodos para generar numeros aleatorios
import threading ##Hilos
import os ##Caracterizticas del sistema operativo

from pupil_tracker import eye_tracker

global x_cuadro, y_cuadro, flag_cuadro
x_cuadro=0
y_cuadro=0
flag_cuadro=True

def loadImage(nombre):
    ruta = os.path.join('Images',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

def GUI_TEST():
    #creo ventana principal
    ventana_principal = Tk()
    ventana_principal.title("GUI test")
    ventana_principal.minsize(680,400)
    ventana_principal.resizable(width=NO,height=NO)
    fondo = Canvas(ventana_principal , width=680,height=400, bg = "#FFFFFF")
    fondo.place(x=0,y=0)

    def stoper():
        global flag_cuadro
        flag_cuadro=False

    def cuadro():
        global x_cuadro, y_cuadro    
        while flag_cuadro:
            Mondrian = loadImage("bola.gif")
            LabelFondo=Label(ventana_principal, image=Mondrian, bg = "#FFFFFF")
            LabelFondo.place (x=x_cuadro, y=y_cuadro)  
            time.sleep(0.3)

    def getCoords():
        global x_cuadro, y_cuadro
        myET = eye_tracker(1)
        listOfImages = ['1.jpg','2.jpg','3.jpg', '4.jpg', '5.jpg']
        while True:
            for image in listOfImages:
                x_cuadro,y_cuadro=myET.pupilDetect('./Images/' +image)
                #print('image, x , y ', image, x_cuadro, y_cuadro)
            # if(x_cuadro != None and y_cuadro != None):
                #    myET.decodify(x_cuadro+50,y_cuadro+53)

    def start():
        #IniciarHilo
        a = Thread(target=cuadro, args=())
        a.start()
        #IniciarHilo
        b = Thread(target=getCoords, args=())
        b.start()
        ventana_principal.mainloop()

    start()

try:
    GUI_TEST()
except:
    print("Error")
    exit()
