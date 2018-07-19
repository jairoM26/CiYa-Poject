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

'''
 * @brief funcion que detecta la pupila
 * 
 * @param imageName:parametro tipo string simple (''), el cual describe el nombre de la imagen a procesar
 * ejemplo de ejecucion: pupilDetect('myImage.jpg')
 * @return void
'''
def pupilDetect(pImageName):
    imageToTrack = cv2.imread(pImageName,0) #open image to track

    backUpImage = imageToTrack.copy() #made a backup of the image

    imageToTrack = cv2.medianBlur(imageToTrack, 49) #apply the medianBlur function to the image to process
    
    contours = cv2.findContours(imageToTrack,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]    

    if len(contours) >= 1:      #get largest blob
        maxArea = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > maxArea:
                maxArea = area
                largeBlob = cnt
            
    if len(largeBlob) > 0:  
        center = cv2.moments(largeBlob)
        if (center['m00']) != 0: # Se agrega un if para evitar division por cero 
            cx,cy = int(center['m10']/center['m00']), int(center['m01']/center['m00'])
            print(cx,cy)
            cv2.circle(backUpImage,(cx,cy),10,255,-1)
        

    #print("x: ", cx, " y: ", cy)
    #show picture
    cv2.imshow('Result',backUpImage) 
    cv2.waitKey(0)   
    cv2.destroyAllWindows()

########## PRUEBA ###############
pupilDetect('prueba4.jpeg')