import cv2
import os
import numpy as np
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

#Đọc ảnh
image1 = cv2.imread('1.jpg')
image2 = cv2.imread('2.jpg')

#Xuất ảnh
#cv2.imshow("Anh 1",image1)
#cv2.imshow("Anh 2",image2)
#cv2.waitKey(0)

#lấy kích thước của ảnh:
h1,w1,c1 = image1.shape
h2,w2,c2 = image2.shape

#Lưu vào h chiều cao, w chiều rộng nhỏ nhất giữa 2 ảnh:
#h=min(h1,h2)
#w=min(w1,w1)
h=480
w=480

#Thay đổi kích thước ảnh theo w,h:
img1 = cv2.resize(image1,(w,h))
img2 = cv2.resize(image2,(w,h))
Speed = 5

for d in range(0,w//2,Speed):
    for l in range(0,h//2,Speed):
        result=img1.copy()
        result[:,w//2-d:w//2+d,:] = img2[:,w//2-d:w//2+d,:]
        result[h//2-d:h//2+d,:,:] = img2[h//2-d:h//2+d,:,:]
        result[:,0:w//2-d,:] = img1[:,0:w//2-d ,:]
        result[0:h//2-d,:,:] = img1[0:h//2-d,:,:]
        result[:,w//2+d:w,:] = img1[:,w//2+d:w,:]
        result[w//2+d:w,:,:] = img1[w//2+d:w,:,:]
    cv2.imshow("Square",result)
    cv2.waitKey(10)