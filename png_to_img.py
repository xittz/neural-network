from PIL import Image
import os, sys

im = Image.open("numbers.png")
rgb_im = im.convert("RGB")
rgb_im.save("numbers.jpg")