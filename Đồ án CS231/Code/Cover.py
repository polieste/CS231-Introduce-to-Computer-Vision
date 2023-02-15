import cv2
import os

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
for d in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:d,:]=img1[:,w-d:w,:]
    result[:,d:w,:]=img2[:,0:w-d]
    cv2.imshow("Cover",result)
    cv2.waitKey(10)