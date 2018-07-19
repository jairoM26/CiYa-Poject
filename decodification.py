# coding=utf-8
'''
 * pupil-tracker.py
 * @brief Programa para detectar la posicion de la pupila en el ojo
 * 
 * @details Este programa utiliza la biblioteca OpenCv version 2 para la realizacion de operaciones
 *          sobre la imagenes. Pasos de ejecucion del programa. Ademas utiliza numpy la cual es una
 *          biblioteca que se utiliza para realizar operaciones matematicas complejas.
 *            
 *          Codigo basado en:
 *          1- https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
 *          2- https://gist.github.com/edfungus/67c14af0d5afaae5b18c
 *  
 *
 *          Pasos del algoritmo:       
 *          1. En este caso el programa se encarga de cargar una imagen especifica en escala de grises 
 *          2. Se hace una copia de esta imagen para mantener la imagen original intacta
 *          3. Se le aplica a la imagen original mediaBlur, funcion de OpenCv a la imagen descrita anteriormente, para asi
 *             poder eliminar el ruido de la imagen.
 *          4. 
 *          
 *
 * @author LuisDiego Delgado Alfaro <>
 * @author JuanDiego Delgado Vargas <>
 * @author JeanCarlos Gonzales Hernandez <>
 * @author Mariana Guerrero Jimenez <>
 * @author Jairo Mendez Martinez <jairomendezmartinez@gmail.com>
 * @date 16-07-2018

'''

import cv2
import numpy as np
from Constants import *

'''
 * @brief funcion para decodificar
 * 
 * @param pX: int corresponding to the x coord
 * @param pY: int corresponding to the y coord
 *
 * @return: the instruction code to execute
 *          0 = center
 *          1 = right
 *          2 = left
 *          3 = up
 *          4 = down 
 *
 *

'''
def decodeCoords(pX, pY):
    if(pX <= initial_coord[0] and pX >= 10 and
        pX >= initial_coord[0] and pX >= 10 and
        pY <= initial_coord[1] and pY >= 10 and
        pY >= initial_coord[1] and pY >= 10):
        return (0,' center')
    elif(pX < initial_coord[0]):
        return (1,' right')
    elif(pX > initial_coord[0]):
        return (1,' left')
    else:
        return