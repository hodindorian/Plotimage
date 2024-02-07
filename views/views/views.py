from django.shortcuts import render
from src.methods import *


def homepage_render(request):
    page = render(request,"homepage.html")
    return page


def black_and_white(request):
    img = import_img()
    if(img!=None):
        img_bw = black_and_white_convert(img)
        page = render(request, "tmp.html", {"img_bw": img_bw})
    else:
        page = render(request,"homepage.html")
    return page

