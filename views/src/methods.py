from PIL import Image
from PIL import ImageSequence
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog as fd
import os


def import_img():

    dossier_telechargement = os.path.expanduser("~/Downloads")

    chemin_image = fd.askopenfilename(
        title="Sélectionner une image",
        initialdir=dossier_telechargement,
    )


    if not chemin_image:
        print("Opération annulée.")
        return None

    extensions_image = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    if not any(chemin_image.lower().endswith(ext) for ext in extensions_image):
        print("Le fichier sélectionné n'est pas une image valide.")
        return None


    try:
        image = Image.open(chemin_image)
        print("Image ouverte avec succès.")
    except IOError:
        print("Erreur lors de l'ouverture du fichier en tant qu'image.")
        image = None

    return image

def black_and_white_convert(img):
    img = img.convert('L')
    return img.point(lambda p: p > 128 and 255)

def grey_convert(img):
    img = img.convert("L")
    return img

def resizePicture(img,width,height):
    img = img.resize((width,height),Image.Resampling.LANCZOS)
    return img

def alignVertically(img1,img2):
    width1,height1 = img1.size
    width2,height2 = img2.size

    imgFinal1 = resizePicture(img1,max(width1,width2),max(height1,height2))
    finalWidth,finalHeight = imgFinal1.size
    imgFinal2 = resizePicture(img2,finalWidth,finalHeight)

    imageVertical = Image.new("RGBA",(finalWidth*2,finalHeight),(0, 0, 0, 0))
    imageVertical.paste(imgFinal1)
    imageVertical.paste(imgFinal2,(finalWidth,0))

    return imageVertical

def alignHorizontally(img1,img2):
    width1,height1 = img1.size
    width2,height2 = img2.size

    imgFinal1 = resizePicture(img1,max(width1,width2),max(height1,height2))
    finalWidth,finalHeight = imgFinal1.size
    imgFinal2 = resizePicture(img2,finalWidth,finalHeight)

    imageHorizontal = Image.new("RGBA",(finalWidth,finalHeight*2),(0, 0, 0, 0))
    imageHorizontal.paste(imgFinal1)
    imageHorizontal.paste(imgFinal2,(0,finalHeight))

    return imageHorizontal

def mixColor(img1,img2,mix=0.5):
    width1,height1 = img1.size
    width2,height2 = img2.size
    imgFinal1 = resizePicture(img1,max(width1,width2),max(height1,height2))
    finalWidth,finalHeight = imgFinal1.size
    imgFinal2 = resizePicture(img2,finalWidth,finalHeight)

    imgFinal1 = imgFinal1.convert("RGB")
    imgFinal2 = imgFinal2.convert("RGB")

    tabImg1 = np.array(imgFinal1)
    tabImg2 = np.array(imgFinal2)
    lenImgTab1 = len(tabImg1)
    lenImgTabIndex0 = len(tabImg1[0])
    final = tabImg1.copy()

    for i in range(0,lenImgTab1):
        for j in range(0,lenImgTabIndex0):
            final[i][j][0] = tabImg1[i][j][0]* mix + tabImg2[i][j][0] * (1-mix)
            final[i][j][1] = tabImg1[i][j][1]* mix + tabImg2[i][j][1] * (1-mix)
            final[i][j][2] = tabImg1[i][j][2]* mix + tabImg2[i][j][2] * (1-mix)

    return Image.fromarray(final)


def gifCreator(listeImage):
    width, height = listeImage[0].size

    for i in range(len(listeImage[1:])):
        listeImage[i+1] = listeImage[i+1].convert('RGB')
        listeImage[i+1] = resizePicture(listeImage[i+1],width,height)

    listeImage[0].save("./views/templates/static/pictures/generated/tmp.gif", save_all=True, append_images=listeImage[1:], loop=0, duration=3000)
