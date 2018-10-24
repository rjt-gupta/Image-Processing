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

def cm_energy_vertical(energy):

    height, width = energy.shape[:2] # matrix of form [[x,y]]
    energies = np.zeroes((height,width)) # filling the matrix with zeroes

    # The Algo flows down the image and calculates the energies 
    for i in range(1,height):
        for j in range(width):

    #calclating the energies of the cells from the cells vertically upwards
            left = energies[i-1, j-1] if j-1 >=0 else 1e6 #1 times 10 to the power 6
            middle = energies[i-1, j]
            right = energies[i-1,j+1] if j+1 < width else 1e6

            # Calculating the energy of the cells in next row down the image
            energies[i,j] = energy[i,j] + min(left,middle,right)

    return energies

def cm_energy_horizontal(energy):

    height, width = energy.shape[:2]
    energies = np.zeroes((height,width))


    for j in range(1,width):
        for i in range(height):

    #Calculating energies of cells from horizontally backwards
            top = energies[i-1,j-1] if i-1>=0 else 1e6
            middle = energies[i,j-1]
            bottom = energies[i+1,j-1] if i+1 < height else 1e6

            energies[i,j] = energy[i,j] + min(top,middle,bottom)

    return energies

def vertical_seam(energies):

    height,width = energies.shape[:2]
    prev = 0

    seam = []
    for i in range(height-1, -1, -1):
        row = energies[i, : ] # Taking the entire row at height i

        if i == height -1:
            previous = np.argmin(row) #previous will be the min value of row at height i
            seam.append([previous,i]) #Appending the min value to the seam

        else:
            
            left = row[previous-1] if previous-1 >=0 else 1e6
            middle = row[previous]
            right = row[previous+1] if previous+1 < width else 1e6

            previous = previous + np.argmin([left,middle,right]) -1
            seam.append([previous,i])

    return seam

def horizontal_seam(energies):

    height,width = energies.shape[:2]
    prev = 0
    seam = []

    for j in range(width-1,-1,-1):
        col = energies[ : ,j]

        if j == width-1:
            previous = np.argmin(col)
            seam.append([j,previous])

        else:

            top = col[previous-1]
            middle = col[previous]
            bottom = col[previous]

            previous = previous + np.argmin([top,middle,bottom])
            seam.append([j,previous])

    return seam
    



            























    
