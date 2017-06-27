import pytesseract
import sys
from PIL import Image, ImageGrab, ImageEnhance, ImageFilter

x1=int(sys.argv[1])
y1=int(sys.argv[2])
x2=int(sys.argv[3])
y2=int(sys.argv[4])
im =ImageEnhance.Contrast(ImageGrab.grab((x1,y1, x2, y2)).filter(ImageFilter.MedianFilter())).enhance(2).convert('1')
text =  pytesseract.image_to_string(im)
print(text)

