import cv2
from PIL import Image
import os, sys

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "numbers.png"
        cv2.imwrite(img_name, frame)
        im = Image.open("numbers.png")
        rgb_im = im.convert("RGB")
        rgb_im.save("numbers.png")
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()