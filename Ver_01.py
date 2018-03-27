#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:30:02 2018

@author: tianshiwei
"""

import cv2
import numpy as np

img = cv2.imread("2-10090.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(3,3),0) 
edges = cv2.Canny(gray, 10, 200)
ls = cv2.HoughLinesP(edges,1,np.pi/180,30,minLineLength=100,maxLineGap=10)
l = ls[:,0,:]
for x1,y1,x2,y2 in l[:]:
    cv2.line(img,(x1,y1),(x2,y2),(0,0,225),2)
cv2.imshow('img',img)
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()