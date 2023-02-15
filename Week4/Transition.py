from turtle import width
import cv2
import numpy as np
import glob
import os
import random

#NHAN 'q' DE DUNG VIDEO
class Image:
    def __init__(self, filename, time=1000, size=500):
        self.size = size
        self.time = time
        self.shifted = 0.0
        self.img = cv2.imread(filename)
        self.height, self.width, _ = self.img.shape
        if self.width < self.height:
            self.height = int(self.height*size/self.width)
            self.width = size
            self.img = cv2.resize(self.img, (self.width, self.height))
            self.shift = self.height - size
            self.shift_height = True
        else:
            self.width = int(self.width*size/self.height)
            self.height = size
            self.shift = self.width - size
            self.img = cv2.resize(self.img, (self.width, self.height))
            self.shift_height = False
        self.delta_shift = self.shift/self.time

    def reset(self):
        if random.randint(0, 1) == 0:
            self.shifted = 0.0
            self.delta_shift = abs(self.delta_shift)
        else:
            self.shifted = self.shift
            self.delta_shift = -abs(self.delta_shift)

    def get_frame(self):
        if self.shift_height:
            roi = self.img[int(self.shifted):int(self.shifted) + self.size, :, :]
        else:
            roi = self.img[:, int(self.shifted):int(self.shifted) + self.size, :]
        self.shifted += self.delta_shift
        if self.shifted > self.shift:
            self.shifted = self.shift
        if self.shifted < 0:
            self.shifted = 0
        return roi


def process():
    path = "pics"
    filenames = glob.glob(os.path.join(path, "*"))

    cnt = 0
    images = []
    for filename in filenames:
        print(filename)

        img = Image(filename)

        images.append(img)
        if cnt > 300:
            break
        cnt += 1

    prev_image = images[random.randrange(0, len(images))]
    prev_image.reset()

    width=500
    height = 500
    video = cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc('M','J','P','G'),60,(width,height))
    while True:
        while True:
            img = images[random.randrange(0, len(images))]
            if img != prev_image:
                break
        img.reset()

        for i in range(100):
            alpha = i/100
            beta = 1.0 - alpha
            dst = cv2.addWeighted(img.get_frame(), alpha, prev_image.get_frame(), beta, 0.0)

            cv2.imshow("Slide", dst)
            video.write(dst)
            if cv2.waitKey(1) == ord('q'):
                return

        prev_image = img
        for _ in range(100):
            frame = img.get_frame()
            cv2.imshow("Slide", frame)
            video.write(frame)
            if cv2.waitKey(1) == ord('q'):
                return

    video.realease()
process()
#NHAN 'q' DE DUNG VIDEO