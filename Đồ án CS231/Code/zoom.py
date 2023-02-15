from scipy.ndimage import rotate
from scipy.ndimage import zoom
import numpy as np
import cv2
import imutils
from PIL import Image
import random
import time
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

class Animations:
    #dán tất cả các hình ảnh phóng to lên trên hình ảnh mờ và tạo một chuỗi các hình ảnh đó
    def img_animation_zoom_in(self, orig_img, blur, fr=30):
        big_img_size = blur.shape
        ret_img = []

        img_list = self.zoom_in_until(blur, orig_img.copy())

        for iimg, img_resz in enumerate(img_list):
            sml_img_size = img_resz.shape
            y_offset = int((big_img_size[1] - sml_img_size[1]) / 2)
            x_offset = int((big_img_size[0] - sml_img_size[0]) / 2)
            im = Image.fromarray(img_resz).convert('RGBA')
            blur_im = Image.fromarray(blur).convert('RGBA')

            # paste rotated image on blur background
            blur_im.paste(im, (y_offset, x_offset), im)
            ret = np.array(blur_im.convert('RGB'))
            ret_img.append(ret)
        return ret_img

    #phóng to hình ảnh
    def zoom_in_until(self, img1, img2):
       
        scale = 0.9
        ret_img = []
        orig_img = img2.copy()
        ((h1, w1), (h2, w2)) = (img1.shape[:2], img2.shape[:2])
        w2f = int(w1 * scale)
        h2f = int(h1 * scale)

        #thay đổi tỉ lệ hình ảnh gốc để chia số lần phóng to
        h2 = int(h1 * 0.7)
        w2 = int(w1 * 0.7)
        img2 = imutils.resize(image=orig_img, height=h2, inter=INTERPOLATION)
        ret_img.append(img2.copy())

        while w2 < w2f and h2 < h2f:
            h2old = h2
            h2 = int(h2 * 1.0018)
            if h2old == h2:
                h2 += 2
            img2 = imutils.resize(image=orig_img, height=h2, inter=INTERPOLATION)
            ret_img.append(img2.copy())

        return ret_img

    def get_blur_img(self, orig_img, big_img_size):
        #thay đổi kích thước thành kích thước lớn
        blur = cv2.resize(orig_img, big_img_size, cv2.INTER_AREA)
        #thu phóng ảnh 1.5 lần sau đó áp dụng hiệu ứng mờ
        blur = self.clipped_zoom(blur, 1.5)
        blur = cv2.blur(blur, (100, 100))
        return blur

    def clipped_zoom(self, img, zoom_factor, **kwargs):
        h, w = img.shape[:2]
        zoom_tuple = (zoom_factor,) * 2 + (1,) * (img.ndim - 2)

        # zoom out
        if zoom_factor < 1:
            zh = int(np.round(h * zoom_factor))
            zw = int(np.round(w * zoom_factor))
            top = (h - zh) // 2
            left = (w - zw) // 2

            out = np.zeros_like(img)
            out[top:top + zh, left:left + zw] = zoom(img, zoom_tuple, **kwargs)

        # zoom in
        elif zoom_factor > 1:
            zh = int(np.round(h / zoom_factor))
            zw = int(np.round(w / zoom_factor))
            top = (h - zh) // 2
            left = (w - zw) // 2

            out = zoom(img[top:top + zh, left:left + zw], zoom_tuple, **kwargs)

            #cắt bỏ các pixels thừa ở các cạnh
            trip_top = ((out.shape[0] - h) // 2)
            trim_left = ((out.shape[1] - w) // 2)
            out = out[trip_top:trip_top + h, trim_left:trim_left + w]

        else:
            out = img

        return out

    def rotateImage(self, img, times=12, scale=10):
        retImg = []
        for i in range(times):
            img = rotate(img, i * scale, reshape=False)
            retImg.append(img)
        return retImg

    def zoomInImage(self, img, times=5, scale=10):
        retImg = []
        for i in range(times):
            img = self.clipped_zoom(img, 1 + i / scale)
            retImg.append(img)

        return retImg

    def zoomOutImage(self, img, times=5, scale=10):
        retImg = []
        for i in range(times):
            img = self.clipped_zoom(img, 1 - i / scale)
            retImg.append(img)

        return retImg

    def fillInBlurry(self, origImg, imgSmallSize=(1000, 500), imgBigSize=(1200, 700), y_offset=100, x_offset=100):
        #thay đổi kích thước thành kích thước lớn
        blur = cv2.resize(origImg, imgBigSize, cv2.INTER_AREA)
        #thu phóng ảnh 1.5 lần sau đó áp dụng hiệu ứng mờ
        blur = self.clipped_zoom(blur, 1.5)
        blur = cv2.blur(blur, (100, 100))

        imgResize = cv2.resize(origImg, imgSmallSize, interpolation=cv2.INTER_AREA)
        blur[y_offset:y_offset + imgResize.shape[0], x_offset:x_offset + imgResize.shape[1]] = imgResize
        return blur

    def trans_fill_in_blurry(self, orig_img, big_img_size=(1200, 700)):
        scale = 0.7
        sml_img_size = (int(big_img_size[0] * scale, int(big_img_size[1] * scale)))
        #thay đổi kích thước thành kích thước lớn
        blur = cv2.resize(orig_img, big_img_size, interpolation=cv2.INTER_AREA)
        #thu phóng ảnh 1.5 lần sau đó áp dụng hiệu ứng mờ
        blur = self.clipped_zoom(blur, 1.5)
        blur = cv2.blur(blur, (100, 100))

        ret_img = []

        while sml_img_size[0] < big_img_size[0] * 0.8 and sml_img_size[1] < sml_img_size[1] * 0.8:
            img_resz = cv2.resize(orig_img, big_img_size, interpolation=cv2.INTER_AREA)
            blur_copy = blur.copy()
            y_offset = int((big_img_size[1] - sml_img_size[1]) / 2)
            x_offset = int((big_img_size[0] - sml_img_size[0]) / 2)

            try:
                blur_copy[y_offset:y_offset + img_resz.shape[0], x_offset:x_offset + img_resz.shape[1]] = img_resz
            except ValueError as e:
                print(e)
                break

            ret_img.append(blur_copy)
            sml_img_size = (sml_img_size[0] + 5, sml_img_size[1] + 5)

        return ret_img

    def left_to_right(self, orig_img, img_big_size=(1200, 700)):
        #thay đổi kích thước thành kích thước lớn
        blur = cv2.resize(orig_img, img_big_size, cv2.INTER_AREA)
        #thu phóng ảnh 1.5 lần sau đó áp dụng hiệu ứng mờ
        blur = self.clipped_zoom(blur, 1.5)
        blur = cv2.blur(blur, (100, 100))

        scale = 0.7
        sml_img_size = (int(img_big_size[0] * scale), int(img_big_size[1] * scale))
        img_resz = cv2.resize(orig_img, sml_img_size, cv2.INTER_AREA)
        i = 0
        ret_img = []

        while True:
            i += 10
            if i > 1000:
                break

            blur_copy = blur.copy()
            x_offset = int((blur_copy.shape[0] - img_resz.shape[0]) / 2)
            try:
                blur_copy[x_offset:x_offset + img_resz.shape[0],
                blur_copy.shape[1] - i:blur_copy.shape[1]] = img_resz[:0:i]
            except ValueError as e:
                print(e)
                break
            ret_img.append(blur_copy)
        return ret_img

    def transparent_to_full(self, prev_img, next_img, alpha=0.1):
        return cv2.addWeighted(prev_img, alpha, next_img, 1 - alpha, 0)

size = (1080, 720)
INTERPOLATION = cv2.INTER_LINEAR
frame_rate = 30
WHITE = (255, 255, 255)
INTERPOLATION = cv2.INTER_LINEAR
start = time.time()
anim = Animations()
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
file_name = "output.avi"
images = [r"1.jpg",r"2.jpg"]

out = cv2.VideoWriter(file_name, fourcc, frame_rate, size)

for iimgs, img_path in enumerate(images):
    img = cv2.imread(img_path)
    print(img_path)
    (h,w) = img.shape[:2]

    img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=WHITE)
    blur = anim.get_blur_img(img,size)
    scale = 0.02
    img_big_size = (int(size[0] * scale, int(size[1] * scale)))
    for i in anim.img_animation_zoom_in(img, blur):
        out.write(i)
    #for i in anim.left_to_right(img,img_big_size):
        #out.write(i)
    #for i in anim.trans_fill_in_blurry(img, img_big_size):
       # out.write(i)

out.release()