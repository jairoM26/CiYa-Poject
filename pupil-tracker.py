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
 *          1- https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
 *          2- https://stackoverflow.com/questions/39167828/eye-pupil-tracking-using-hough-circle-transform
 *  
 *
 *          Pasos del algoritmo:       
 *          1. En este caso el programa se encarga de cargar una imagen especifica, 
 *          2. Se hace una copia de esta imagen para poder obtenerla en escala de grises, y permanecer
 *             la imagen original intacta
 *          3. Se le aplica a la imagen en escala de grises la funcion CLAHE (Contrast Limited Adaptive 
 *             Histogram Equalization) la cual se encarga de aplicarle una ecualizacion de histograma con 
 *             contraste. https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html
 *          4. Luego se le aplica mediaBlur funcion de OpenCv a la imagen descrita anteriormente, para asi
 *             poder eliminar el ruido de la imagen.
 *          5. Luego se le aplica la funcion de HoughCircles, la cual se encarga de de encontrar circulos
 *             en escala de grises mediante el uso de la transformada de Hough. https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html?highlight=houghcircles
 *          6. Luego de aplicar lo del tutorial [1] para dibujar circulos, se muestran las imagenes resultantes
 *             y se liberan recursos cuando se cierren.
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

    #This method usually increases the global contrast of many images, especially 
    # when the usable data of the image is represented by close contrast values. 
    # Through this adjustment,the intensities can be better distributed on the histogram.
    #imageToTrack =cv2.equalizeHist(imageToTrack) # do the equalizeHist
    
    #aplicar filtro de blanco y negro a la imagen
    ret, imageToTrack = cv2.threshold(imageToTrack,0,255,cv2.THRESH_BINARY)  
    
    threshold = cv2.inRange(imageToTrack,250,255)     #get the blobs
    
    contours = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[1]    

    if len(contours) >= 2:
        #find biggest blob
        maxArea = 0
        MAindex = 0         #to get the unwanted frame 
        distanceX = []      #delete the left most (for right eye)
        currentIndex = 0 
        for cnt in contours:
            area = cv2.contourArea(cnt)
            center = cv2.moments(cnt)
            if (center['m00'] !=0 ): # Evita la división por cero
                cx,cy = int(center['m10']/center['m00']), int(center['m01']/center['m00'])
                distanceX.append(cx)    
            if area > maxArea:
                maxArea = area
                MAindex = currentIndex
            currentIndex = currentIndex + 1

        del contours[MAindex]       #remove the picture frame contour
        del distanceX[MAindex]

    if len(contours) >= 2:      #delete the left most blob for right eye
        edgeOfEye = distanceX.index(max(distanceX)) 
        del contours[edgeOfEye]
        del distanceX[edgeOfEye]

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
    cv2.destroyAllWindows()

########## PRUEBA ###############
pupilDetect('prueba4.jpeg')