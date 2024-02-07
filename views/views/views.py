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
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "black_and_white.html", context)
    else:
        page = render(request,"homepage.html")
    return page


def grey(request):
    img = import_img()
    if(img!=None):
        print("test")
        img_bw = grey_convert(img)
        context = {
            'img_str': img_bw,
        }
        img_bw.save("./views/templates/static/pictures/tmp.jpg")
        page = render(request, "grey.html", context)
    else:
        page = render(request,"homepage.html")
    return page
