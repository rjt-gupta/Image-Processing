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

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Till now we blurred the image by gaussian and converted to grayscale
# Then Sobel filters are applied to calc x and y grads separately
# Next we add absolut values of those grads to get the final energy function


def energy(img):
    blurred = gaussian_blur(img)
    gray = grayscale(blurred)
    dx = x_grad(gray)
    dy = y_grad(gray)

    return cv2.add(np.absolute(dx), np.absolute(dy))
    



            























    
