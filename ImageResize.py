#Resizing an image with Pillow python
#Author Luis Diego Delgado Alfaro
#Juan Diego Delgado Vargas
#Jairo Mendez Martinez
#Mariana Guerrero Jimenez
#Jean Carlos Gonzales Hernandez


#First, you need to install the Python Pillow library

from PIL import Image

'''
@brief Resize: Function that creates a thumbnail of an image. Those are reduced-size versions of pictures but still contains all of the most important aspects of the image. 
@param pImageToResize image to be load, string type. 
@param pX, pY, size of the image in the X and Y axis. Integer type. 
@pImageNameSave: Image saved after the thumbnail process. String type

@details:
	Based on:Python for beginners "How to use a Pillow, a fork of 		PIL" https://www.pythonforbeginners.com/gui/how-to-use-pillow
		
'''
def Resize(pImageToResize, pX, pY, pImageNameSave):
    size = (pX, pY) #Size of the final resize image
    try:
        im = Image.open(pImageToResize)#Load the image
        print(im.format,im.size,im.mode) #Original size,format and mode of the image
    except:
        print ("Unable to load image") #In case that we couldnt load it, print this message

    im.thumbnail(size) #Create the thumbnail image
    im.save(pImageNameSave) #Save the thumbnail image
    im.show()
    #In case that we want to see the caracteristics of the image, use this:
    #im2 = Image.open("ImageSaved.jpg")
    #print(im2.format,im2.size,im2.mode) #Final size,format and mode of the image
   
