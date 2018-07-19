'''
 * Convert.py
 * @brief Programa para convertir imagen a serial
 * 
 * @details Se convierte imagen a serial mediante el algoritmo de conversion de base 64
 *            
 * @author LuisDiego Delgado Alfaro <>
 * @author JuanDiego Delgado Vargas <>
 * @author JeanCarlos Gonzales Hernandez <>
 * @author Mariana Guerrero Jimenez <>
 * @author Jairo Mendez Martinez <jairomendezmartinez@gmail.com>
 * @date 16-07-2018
'''
import base64

'''
 * @brief convierte imagen a string
 *
 * @param pImageName: tipo string que indica el nombre de la imagen a convertir
 *
 * @return string de la conversion
'''
def convertImageToString(pImageName):
    with open(pImageName, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        return str

'''
 * @brief convierte string a imagen
 *
 * @param pEntryString: tipo string que quiere convertirse a imagen
 * @param pImageName: tipo string que indica el nombre de la imagen donde se quiere guarda la conversion
 *
 * @return string de la conversion
'''
def convertStringToImage(pEntryString, pImageName):
    fh = open(pImageName, "wb")
    fh.write(pEntryString.decode('base64'))
    fh.close()
