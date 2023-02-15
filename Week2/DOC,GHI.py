#---------------DOC GHI---------------
#DOC ANH
import cv2
img = cv2.imread('ttnt.jpg')
print("Cao %d pixel, rong: %d pixel, %d kenh mau." % (img.shape[0], img.shape[1], img.shape[2]))
#GHI ANH
img = cv2.imread('ttnt.jpg', 0)
cv2.imwrite('huyhuy.png', img)
#HIEN THI ANH
cv2.imshow('Minh Huy image', img)
cv2.waitKey(0)
