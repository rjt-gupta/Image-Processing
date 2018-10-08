import cv2
from cv2 import cv
import numpy as np

import sys


# gaussian filter to blur the image(reducing the noise)
def gaussian_blur(img):
    return cv2.GaussianBlur(img (3,3),0,0)

# Sobel filter (input, output, img_prop*) to calc x gradient
def x_grad(img):
    return cv2.Sobel(img, cv2.CV_64F,1,0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)


# Calc y gradient from Sobel filter 
def y_grad(img):

    return cv2.Sobel(img, cv2.CV_64F,0,1, ksize=3,scale=1, delta=0, borderType=BORDER_DEFAULT)


    



            























    
