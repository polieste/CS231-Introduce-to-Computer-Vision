import cv2
import numpy as np
# B1: Load anh
I = cv2.imread("hienho.jpeg", 0)

# B2: Hien thi anh
cv2.imshow("Hien ho", I)

# B3: Filter anh
filter1 = np.array(
    [[1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]])
filter2 = np.array(
    [[1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]])

def max_pooling(I, kernel_size=2):
    pass

def avg_pooling(I, kernel_size=2):
    pass
def median_pooling(I, kernel_size=2):
    pass

def edge_detection(I, filter):
    result1 = cv2.filter2D(I, -1, filter)
    result2 = cv2.filter2D(I, -1, filter.T)
    result3 = cv2.filter2D(I, -1, -filter)
    result4 = cv2.filter2D(I, -1, -filter.T)
    return result1 + result2 + result3 + result4

result1= edge_detection(I, filter1)
result2= edge_detection(I, filter2)

# B4: Hien thi anh sau filter
#cv2.imshow("Hien ho after effect 1", result1)
#cv2.imshow("Hien ho after effect 2", result2)
cv2.imshow("Hien ho after effect 1", result1)
cv2.imshow("Hien ho after effect 2", result2)
cv2.waitKey(0)
