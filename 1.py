import cv2
import numpy as np
import math
import random

def calculo1(img,conv):
    tam = img.shape[0]
    suma = 0
    for i in range (tam):
        for j in range (tam):
            suma +=img[i,j]*conv[i,j]
    return suma


def convolution(filename, M):
    imgc = cv2.imread(filename)
    Y = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)
    #Y = np.arange(50).reshape(5,10)
    #M = np.array([[1,0,-1],[0,-1,0],[-1,0,1]])
    cols, rows = Y.shape[:2]
    output = np.zeros((cols,rows), np.uint8)
    #print(Y,'\n',M,'\n',output)
    for i in range (cols-2):
        for j in range (rows-2):
            img = Y[i:3+i,j:3+j]
            output[i+1,j+1] =calculo1(img,M) 
            #print('\n',img,'\n',M,'\n',output) 
            #print("rpta: ", calculo1(img,M))
    strr = "rotation_"+str(random.random())+".jpg"
    cv2.imwrite(strr,output)

filename = askopenfilename()
vmin = -1
vmax = 1
for i in range(vmin,vmax):
    for i1 in range(vmin,vmax):
        for i2 in range(vmin,vmax):
            for i3 in range(vmin,vmax):
                for i4 in range(vmin,vmax):
                    for i5 in range(vmin,vmax):
                        for i6 in range(vmin,vmax):
                            for i7 in range(vmin,vmax):
                                for i8 in range(vmin,vmax):
                                    M = np.array([[i,i1,i2],[i3,i4,i5],[i6,i7,i8]])
                                    convolution(filename,M)

#rotation(filename,30)
#convolution(filename)
