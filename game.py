from tkinter import *
import os
from threading import Thread
import threading
import random
import time

'''
*  load_img
*  Method that allows the load of an image (png or gif) file.
*  @param name: the name of the file that is inside the imgs directory
*  @returns img: the img load in the respective memory space
'''
def load_img(name):
    path = os.path.join("images",name)
    img = PhotoImage(file = path)
    return img

def game():
    gameWindow = Tk()
    gameWindow.title("Game")
    gameWindow.minsize(350,600)
    gameWindow.resizable(width=False,height=False)
    gameWindow.geometry("350x600")  
    
    car = load_img('car.png')
   # screen = load_img("fondo.png")

    '''#Creation of the canvas for the simulation objects
    contenedor = Canvas(gameWindow, width=350, height=600, bg="#FFFFFF")
    contenedor.place(x=0,y=0)

    screenObj = contenedor.create_image(40,20, image = screen)
    carObj = contenedor.create_image(300,580, image=car)
    '''
    gameWindow.mainloop()

game()