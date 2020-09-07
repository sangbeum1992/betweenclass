from PIL import Image
from pytesseract import *
import re
import cv2

img = Image.open('F:\\timetable\\1.jpg')
text = pytesseract.image_to_string(img, lang = 'kor',)


print(text)