from django.shortcuts import render
from src.methods import *


def homepage_render(request):
    page = render(request,"homepage.html")
    return page


def black_and_white(request):
    img = import_img()
    if(img!=None):
        img_bw = black_and_white_convert(img)
        context = {
            'img_str': img_bw,
        }
        img_bw = img_bw.convert('RGB')
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "black_and_white.html", context)
    else:
        page = render(request,"homepage.html")
    return page


def grey(request):
    img = import_img()
    if(img!=None):
        img_bw = grey_convert(img)
        context = {
            'img_str': img_bw,
        }
        img_bw = img_bw.convert('RGB')
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "grey.html", context)
    else:
        page = render(request,"homepage.html")
    return page

def resizing(request):
    img = import_img()
    if request.method == 'POST':
        width = request.POST.get('width')
        height = request.POST.get('height')
        width = int(width)
        height = int(height)
        if(img!=None):
            print(width,height)
            img_bw = resizePicture(img,width,height)
            context = {
                'img_str': img_bw,
            }
            img_bw = img_bw.convert('RGB')
            img_bw.save("./views/templates/static/pictures/tmp.jpg")
            page = render(request, "resizing.html", context)
        else:
            page = render(request,"homepage.html")
        return page
    else:
        page = render(request,"homepage.html")
        return page

def resizing_first(request):
    return render(request, "resizing_choose.html")



def alignVertical(request):
    img1 = import_img()
    img2 = import_img()
    if(img1!=None and img2!=None):
        img_bw = alignVertically(img1,img2)
        context = {
            'img_str': img_bw,
        }
        img_bw = img_bw.convert('RGB')
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "align_vertical.html", context)
    else:
        page = render(request,"homepage.html")
    return page

def alignHorizontal(request):
    img1 = import_img()
    img2 = import_img()
    if(img1!=None and img2!=None):
        img_bw = alignHorizontally(img1,img2)
        context = {
            'img_str': img_bw,
        }
        img_bw = img_bw.convert('RGB')
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "align_horizontal.html", context)
    else:
        page = render(request,"homepage.html")
    return page

def fusionning(request):
    img1 = import_img()
    img2 = import_img()
    if(img1!=None and img2!=None):
        img_bw = mixColor(img1,img2)
        context = {
            'img_str': img_bw,
        }
        img_bw = img_bw.convert('RGB')
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "fusionning.html", context)
    else:
        page = render(request,"homepage.html")
    return page

def animation(request):
    img1 = import_img()
    img2 = import_img()
    if(img1!=None and img2!=None):
        img_bw = mixColor(img1,img2)
        context = {
            'img_str': img_bw,
        }
        img_bw = img_bw.convert('RGB')
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "fusionning.html", context)
    else:
        page = render(request,"homepage.html")
    return page
