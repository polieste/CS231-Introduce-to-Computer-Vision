#---------------XU LY------------------
import numpy as np
import cv2
import matplotlib.pyplot as plt
#DOC VA IN ANH
img = cv2.imread('ttnt.jpg')
print(type(img))
print(img.shape)
plt.imshow(img,cmap='gray')
plt.show()
#LAY KICH THUOC ANH
(h, w, d) = img.shape
print("width={}, height={}, depth{}".format(w, h, d))
#LAY MAU O 1 DIEM
(B, G, R) = img[50, 50]
print("R={}, G={}, B={}".format(R, G, B))
#XOAY ANH THEO CHIEU DOC
img = cv2.imread('ttnt.jpg',0)
result = img[::-1]
plt.imshow(result, cmap='gray')
plt.show()
#XOAY ANH THEO DUONG CHEO CHINH
result1 = img.transpose()
plt.imshow(result1,cmap='gray')
plt.show()
#XOAY ANH THEO CHIEU NGANG
result2 = img[:,::-1]
plt.imshow(result2,cmap='gray')
plt.show()
#DIEU CHINH DO SANG TOI
result = img.copy()
result = result + 50
plt.imshow(result, cmap='gray')
plt.show()
#DOI MAU MOT VUNG ANH
result = img.copy()
result[100:400, 300:600] = 255
plt.imshow(result,cmap='gray')
plt.show()
