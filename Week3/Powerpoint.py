import cv2
import os

#Đọc ảnh
image1 = cv2.imread('1.png')
image2 = cv2.imread('2.png')

#Xuất ảnh
cv2.imshow("Anh 1",image1)
cv2.imshow("Anh 2",image2)
cv2.waitKey(0)

#lấy kích thước của ảnh:
h1,w1,c1 = image1.shape
h2,w2,c2 = image2.shape

#Lưu vào h chiều cao, w chiều rộng nhỏ nhất giữa 2 ảnh:
h=min(h1,h2)
w=min(w1,w1)

#Thay đổi kích thước ảnh theo w,h:
img1 = cv2.resize(image1,(w,h))
img2 = cv2.resize(image2,(w,h))

#Push
Speed = 5
for d in range(0,h+1,Speed):
    result=img1.copy()
    result[0:h-d,:,:]=img1[d:h,:,:]
    result[h-d:h,:,:]=img2[0:d,:,:]
    cv2.imshow("Push",result)
    cv2.waitKey(10)

#Uncover
Speed = 5
for d in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:w-d,:] = img1[:,d:w,:]
    result[:,w-d:w,:] = img2[:,w-d:w,:]
    cv2.imshow("Uncover",result)
    cv2.waitKey(10)

#Wipe
Speed = 5
for d in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:w-d,:] = img1[:,d:w,:]
    result[:,w-d:w,:] = img2[:,0:d,:]
    cv2.imshow("Wipe",result)
    cv2.waitKey(10)

#Cover    
Speed = 5
for d in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:d,:]=img1[:,w-d:w,:]
    result[:,d:w,:]=img2[:,0:w-d]
    cv2.imshow("Cover",result)
    cv2.waitKey(10)

#Split
Speed = 5
for d in range(0,w//2,Speed):
    result=img1.copy()
    result[:,w//2-d:w//2+d,:] = img2[:,w//2-d:w//2+d,:]
    result[:,0:w//2-d,:] = img1[:,0:w//2-d ,:]
    result[:,w//2+d:w,:] = img1[:,w//2+d:w,:]
    cv2.imshow("Split",result)
    cv2.waitKey(10)