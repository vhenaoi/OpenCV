# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:45:35 2018

@author: lxMera
"""

import cv2

frame=cv2.imread('Virus.png')

cv2.namedWindow('Window',0)

cv2.imshow('Window',frame)

cv2.waitKey(0)

cv2.destroyAllWindows()  

