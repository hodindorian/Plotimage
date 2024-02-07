from PIL import Image
from PIL import ImageSequence
import numpy as np
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def import_img():
    Tk().withdraw()

    chemin_image = askopenfilename(
        title="Sélectionner une image",
        filetypes=[("Fichiers image", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )

    if not chemin_image:
        print("Opération annulée.")
        return None

    # Ouvrir l'image avec PIL
    image = Image.open(chemin_image)
    print("Image ouverte avec succès.")

    return image

def black_and_white_convert(img):
    img = img.convert('L')
    return img.point(lambda p: p > 128 and 255)

def grey(img):
    img = img.convert("L")
    return img

def resizePicture(img,width,height):
    img.thumbnail((width,height))
    return img

def alignVertically(img1,img2):
    width1,height1 = img1.size
    width2,height2 = img2.size

    imgFinal1 = resizePicture(img1,max(width1,width2),max(height1,height2))
    finalWidth,finalHeight = imgFinal1.size
    imgFinal2 = resizePicture(img1,finalWidth,finalHeight)

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

    for image in listeImage[1:]:
        img = resizePicture(image,width,height)
        img = img.thumbnail((width, height))

    listeImage[0].save("animation.gif", save_all=True, append_images=listeImage[1:], loop=0, duration=5000)
