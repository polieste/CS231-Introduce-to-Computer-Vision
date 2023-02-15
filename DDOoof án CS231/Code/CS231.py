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
h=720
w=720

#Thay đổi kích thước ảnh theo w,h:
img1 = cv2.resize(image1,(w,h))
img2 = cv2.resize(image2,(w,h))

Line = 10 # Chia ra thành 10 dòng
h1 = h1 // Line
Speed = 6
for D in range(0, w + 1, Speed):
    result=img1.copy()
    for L in range(0, Line,2):
        result[h1*L:h1*(L+1) :,D:h] = img2[h1*L:h1*(L+1):,0:h - D]
        result[h1*(L+1):h1*(L+2):, 0:h - D] = img2[h1*(L+1):h1*(L+2):, D:h]
    cv2.imshow("Comb", result)
    cv2.waitKey(10)
'''
#Uncover
Speed = 6
for d in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:w-d,:] = img1[:,d:w,:]
    result[:,w-d:w,:] = img2[:,w-d:w,:]
    cv2.imshow("Uncover",result)
    cv2.waitKey(10)

#Cover    
Speed = 6
for d in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:d,:]=img1[:,w-d:w,:]
    result[:,d:w,:]=img2[:,0:w-d]
    cv2.imshow("Cover",result)
    cv2.waitKey(10)

#Split
Speed = 6
for d in range(0,w//2,Speed):
    result=img1.copy()
    result[:,w//2-d:w//2+d,:] = img2[:,w//2-d:w//2+d,:]
    result[:,0:w//2-d,:] = img1[:,0:w//2-d ,:]
    result[:,w//2+d:w,:] = img1[:,w//2+d:w,:]
    cv2.imshow("Split",result)
    cv2.waitKey(10)

#Comb
Line = 10 # Chia ra thành 10 dòng
h1 = h1 // Line
Speed = 6
for D in range(0, w + 1, Speed):
    result=img1.copy()
    for L in range(0, Line,2):
        result[h1*L:h1*(L+1), 0:D, :] = img1[h1*L:h1*(L+1), w - D:w, :]
        result[h1*L:h1*(L+1), D:w, :] = img2[h1*L:h1*(L+1), 0:w - D]
        result[h1*(L+1):h1*(L+2), 0:w - D, :] = img2[h1*(L+1):h1*(L+2), D:w, :]
        result[h1*(L+1):h1*(L+2), w - D:w, :] = img1[h1*(L+1):h1*(L+2), 0:D, :]
    cv2.imshow("Comb", result)
    cv2.waitKey(10)

#Split Comb
Line = 10 # Chia ra thành 10 dòng
h1 = h1 // Line
Speed = 6
for D in range(0, w + 1, Speed):
    result=img1.copy()
    for L in range(0, Line,2):
        result[h1*L:h1*(L+1) :,D:h] = img2[h1*L:h1*(L+1):,0:h - D]
        result[h1*(L+1):h1*(L+2):, 0:h - D] = img2[h1*(L+1):h1*(L+2):, D:h]
    cv2.imshow("Comb", result)
    cv2.waitKey(10)

#Square
Speed = 6
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

#Plus
Speed = 6
for d in range(0,w//2,Speed):
    result=img1.copy()
    for l in range(0,h//2,Speed):  
        result[:,w//2-d:w//2+d,:] = img2[:,w//2-d:w//2+d,:]
        result[h//2-d:h//2+d,:,:] = img2[h//2-d:h//2+d,:,:]
        cv2.imshow("Plus",result)
    cv2.waitKey(10)

#T shape
Speed = 6
for d in range(0,w//2,Speed):
    result=img1.copy()
    result[h//2-d:w//2,:,:] = img2[h//2-d:h//2,:,:]
    result[:,w//2-d:w//2+d,:] = img2[:,w//2-d:w//2+d,:]
    result[0:h//2-d,:,:] = img1[d:h//2,:,:]
    cv2.imshow("Plus",result)
    cv2.waitKey(10)
'''
