#!/usr/bin/env python
# coding: utf-8

# # answer of ques 5

# In[4]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread("Downloads/images.jpg")
cv2.imshow('image', image)


# In[5]:


a=cv2.bitwise_not(image)
plt.imshow(a)
plt.show()


# # answer of ques 4

# In[1]:


import cv2
image=cv2.imread('Downloads/faces.jpg')
cv2.imshow('image',image)


# In[2]:


face_cascade=cv2.CascadeClassifier('C:/Users/dell/Desktop/opencv-master1/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
img=cv2.imread("Downloads/faces.jpg")
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(img,1.3,5)
count_face=str(len(face))
print(count_face)


# # answer of ques 3

# In[ ]:


import cv2
  
originalImage = cv2.imread('Downloads/images.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
blueimage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)

cv2.imshow('Gray image', grayImage)
cv2.imshow('blue image', blueimage)
  
cv2.waitKey(0)
cv2.destroyAllWindows()

