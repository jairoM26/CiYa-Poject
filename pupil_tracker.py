# coding=utf-8
'''
 * pupil_tracker.py
 * @brief Class that include the corresponding methods to extract the position of the pupil 
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
from math import pi, atan2, sqrt, degrees
from Constants import DEBBUG, WIDTH, HEIGHT

class eye_tracker:
    decodifyAlgorithm = None
    '''
    * @brief class constructor
    *
    * @param pType: indicate the decodification algorith type
    '''
    def __init__(self, pType):
        self.decodifyAlgorithm = pType
    '''
    * @brief function to detect the centroid of the pupil
    * 
    * @details
    *          Based on:
    *          1- https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
    *          2- https://gist.github.com/edfungus/67c14af0d5afaae5b18c
    *  
    *
    *          Steps
    *          1. Open image in gray scale
    *          2. resize iage, because the incoming is too small (for our usage)
    *          3. Apply medianBlur filter 
    *          4. Apply an equalize histogram
    *          5. Apply a binary filter to get only white and black color
    * @param imageName:parametro tipo string simple (''), el cual describe el nombre de la imagen a procesar
    * ejemplo de ejecucion: pupilDetect('myImage.jpg')
    * @return centroid of the pupil
    '''
    def pupilDetect(self, pImageName):
        cx = None 
        cy = None
        
        imageToTrack = cv2.imread(pImageName,0) #open image to track   
        
        imageToTrack = cv2.resize(imageToTrack, (WIDTH, HEIGHT))

        backUpImage = imageToTrack.copy()

        imageToTrack = cv2.medianBlur(imageToTrack, 51) #apply the medianBlur function to the image to process

        #This method usually increases the global contrast of many images, especially 
        # when the usable data of the image is represented by close contrast values. 
        # Through this adjustment,the intensities can be better distributed on the histogram.
        imageToTrack =cv2.equalizeHist(imageToTrack) # do the equalizeHist
        
        #apply filter to get only white and black color
        imageToTrack = cv2.threshold(imageToTrack,0,255,cv2.THRESH_BINARY)[1]
        
        #inRange return an array with the corresponding colors value (to apply next filter)
        threshold = cv2.inRange(imageToTrack,255,255) 
        
        #find contuors> its mean that find continuos points with same color or intensity
        contours = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[1]
       
        if(DEBBUG):
                cv2.drawContours(backUpImage, contours, -1, (255,0,255), 3)
                cv2.imshow('Result', backUpImage)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        
        for cnt in contours:         
            #find all the points of the contour   
            center = cv2.moments(cnt)
            perimeter = cv2.arcLength(cnt,True)
            radio = perimeter/(2*pi)
            #TODO find an accurate way to find the real pupil contour            
            if(radio >= 13 and radio <= 29):
                #find the centroid
                if (center['m00'] !=0 ): # Evita la división por cero
                    cx,cy = int(center['m10']/center['m00']), int(center['m01']/center['m00'])

        return cx, cy       

    '''
    * @brief method to decodify the pupil centroid
    * 
    * @details This method can perform 2 diferents algorithms to decodify the pupil centroid
    *          The first one t
    *          The second one (coords(pX, pY)) decodify the x and y pos of the pupil centroid and return
    *          the angle and force corresponding to the coordinate axis, which the point 0, 0 its defined
    *          on the center of the image
    *
    * @param pX: type integer: x position from the img
    * @param pX: type integer: y position from the img
    * 
    * @return if decodifyAlgorithm equal to 0: the instruction of a gestor
    *         if decodifyAlgorithm equal to 1: x, y, angle, force 
    * 
    '''
    def decodify(self, pX, pY):
        #TODO patron recognize algorithm to recognize gestors of the eye
        def gestor():
            return

        def coords(pX, pY):
            #convert coords to axis defined
            pX -= WIDTH/2 
            pY = HEIGHT/2 -pY
            
            #measure and converting angle depending on the coordinate in which the point is
            angle = degrees(atan2(pY,pX))
            if ((pX < 0 and pY < 0) or (pX > 0 and pY < 0)): angle += 360
            elif (pX < 0 and pY > 0): angle += 180 

            #calculating force           
            force = sqrt(pX*pX + pY*pY)
            return pX, pY, angle, force
            
        if (not self.decodifyAlgorithm):
            return gestor()
        elif (self.decodifyAlgorithm):
            return coords(pX, pY)
        
