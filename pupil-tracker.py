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
def pupilDetect(imageName):
    img = cv2.imread(imageName,0)
    img = cv2.medianBlur(img,21)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,40,
                                param1=50,param2=30,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        print("outer circle: x: ",i[0], " y: ", i[1], " r:", i[2])
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

########## PRUEBA ###############
pupilDetect('prueba.jpeg')