import cv2
import numpy as np

# Bước 1: Load ảnh lên và hiển thị ảnh
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting,nếu nút chuột trái được nhấp, hãy bắt đầu ghi lại  (x, y) tọa độ và chỉ ra rằng việc cắt xén đang được thực hiện
    # (x, y) coordinates and indicate that cropping is being,
    # performed,
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released,kiểm tra xem nút chuột trái đã được thả ra chưa
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that,ghi lại tọa độ kết thúc (x, y) và chỉ ra rằng thao tác cắt xén đã hoàn thành
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(img, refPt[0], refPt[1], (0, 0, 255), 2)
        cv2.imshow("Input image", img)

img = cv2.imread('chormmakey.jpg')
img=cv2.resize(img,(800,500))
clone = img.copy()
print(clone.shape)
cv2.imshow("Input image", img)
cv2.setMouseCallback("Input image", click_and_crop)#sau lệnh này img dc đánh dấu lên vùng đã chọn

# Bước 2: Chọn một vài pixel thuộc vùng nền
lst_rois = []
refPt = []
cropping = False
while True:
    # display the image and wait for a keypress,hiển thị hình ảnh và đợi một lần nhấn phím
    cv2.imshow("Input image", img)

    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region,nếu phím 'r' được nhấn, hãy đặt lại vùng cắt
    if key == ord("r"):
        img = clone.copy()
    # if the 'c' key is pressed, break from the loop,nếu phím 'c' được nhấn, ngắt khỏi vòng lặp
    elif key == ord("c"):
        break
# if there are two reference points, then crop the region of interest,nếu có hai điểm tham chiếu, thì hãy cắt vùng quan tâm
#hình dung 2 điểm này là điểm A, C của hình chữ nhật ABCD
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]# (x1,y1) (x2,y2) [x1:x2,y1:y2]
    lst_rois.append(roi.copy())
    cv2.imshow("ROI", roi)
# close all open windows
#cv2.destroyAllWindows()

# Bước 3: Tính giá trị màu đại diện
#vùng xén ra được lưu vào roi
print(roi.shape)
print(roi[0:5,0:5])
r,g,b=np.split(roi,3,-1)
print(r.shape)
print(r[0:5,0:5])
print(g.shape)
print(g[0:5,0:5])
R=np.average(r)
G=np.average(g)
B=np.average(b)
print(R,G,B)
# Bước 4: Tính độ lệch (threshold)
r_=r.flatten()
g_=g.flatten()
b_=b.flatten()
rr=np.var(r_)
gg=np.var(g_)
bb=np.var(b_)
print(rr,gg,bb)
# Bước 5: Bắt đầu phân đoạn ảnh với
# giá trị màu đại diện và độ lệch
new_background=cv2.imread("kho anh/marvel.jpg")
new_background=cv2.resize(new_background,(clone.shape[1],clone.shape[0]))
print("newbacground",new_background.shape)
result=clone.copy()
t=clone.copy()

# chon cac diem ko thoa man, danh dau
t[R-rr>clone[:,:,0]]=0
t[clone[:,:,0]>R+rr]=0
t[G-gg>clone[:,:,1]]=0
t[clone[:,:,1]>G+gg]=0
t[B-bb>clone[:,:,2]]=0
t[clone[:,:,2]>B+bb]=0

result[t[:,:,:]!=0]=new_background[t[:,:,:]!=0]


# Bước 6: THay vùng nền bằng ảnh bất kỳ
cv2.imshow("result",result)
cv2.imwrite("img_after_chorma_key.jpg",result)
cv2.waitKey(0)