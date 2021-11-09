import cv2, os, numpy as np
from PIL import ImageGrab
from typing import List
from os import listdir
from os.path import isfile

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:

        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized


h, w = cv2.imread("C:/Users/Admin/Desktop/Code/wsop/card/T-heart.png", cv2.IMREAD_GRAYSCALE).shape
print(h,w)

mypath = "C:/Users/Admin/Desktop/Code/wsop/cardtest/"
cardfile = [mypath+f for f in listdir(mypath)]
for card in  cardfile:
    use = cv2.imread(card, cv2.IMREAD_GRAYSCALE)
    use = image_resize(use,w,h)
    h, w = use.shape
    print(h,w)
    cv2.imwrite(card.split('/')[-1], use)