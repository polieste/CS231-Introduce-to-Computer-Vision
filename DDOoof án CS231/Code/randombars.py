import cv2
import numpy as np
import random
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

image = cv2.imread(r"1.jpg", cv2.IMREAD_UNCHANGED)

#xuất ảnh
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#lấy kích thước ảnh
width = image.shape[1]
height = image.shape[0]

#xác định video codec
fourcc = VideoWriter_fourcc(*'MP42')

#xác định video stream
video = VideoWriter('video.avi', fourcc, float(24), (width, height))

#khởi tạo khung rỗng
frame = np.zeros((height, width, 3), np.uint8)

#khởi tạo frame count
frame_count = 0

#khởi tạo chỉ mục random row 
random_rows = list(range(len(image)))

#xáo trộn chỉ mục các hàng theo thứ tự ngẫu nhiên
random.shuffle(random_rows)

#loop qua các hàng pixel trong ảnh gốc
for y in random_rows:
    #loop qua các pixels trong 1 hàng nhất định
    for x in range(len(image[y])):
        #sẽ pixel trên khung
        cv2.circle(
            frame,                      #khung để ghi pixel vào
            (x, y),                     #tọa độ tâm của một vòng tròn
            1,                          #bàn kính vòng tròn
            (int(image[y][x][0]),       #giá trị pixel RED 
             int(image[y][x][1]),       #giá trị pixel GREEN 
             int(image[y][x][2])        #giá trị pixel BLUE 
            ),
            -1                          #độ dày
        )

    #ghi khung video
    if (y % 20 == 0):
        frame_count += 1
        video.write(frame)
        print('Writing frame:', frame_count)

#giữ ảnh trong 1 khoảng thời gian...
for i in range(100):
    #write complete frame
    video.write(frame)
    frame_count += 1
    print('Writing frame:', frame_count)

#xuất video
video.release()


   

