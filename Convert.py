import base64

def convertImageToString(imageName):
    with open("Pogbum.jpg", "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        print (str)
        return str

def convertStringToImage(entryString):
    fh = open("imageToSave.png", "wb")
    fh.write(str.decode('base64'))
    fh.close()
