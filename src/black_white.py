def black_and_white(img):
    imgBlackAndWhite = img
    imgBlackAndWhite = imgBlackAndWhite .convert('L')
    imgBlackAndWhite = imgBlackAndWhite.point(lambda p: p > 128 and 255)
    return imgBlackAndWhite
