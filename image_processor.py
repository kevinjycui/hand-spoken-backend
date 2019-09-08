from pytesseract import pytesseract as pt
import PIL
from PIL import Image
from pytesseract import Output
import cv2
import pprint
import os

pt.tesseract_cmd = r'C:\Users\kevin\AppData\Local\Tesseract-OCR\tesseract.exe'

def processImage(filename):
    img = cv2.imread('src/images/'+filename)
    d = pt.image_to_boxes(img, output_type=Output.DICT)
    return d

def cropImages(filename, dir):
    d = processImage(filename)
    img = cv2.imread(filename)
    WIDTH, HEIGHT, _ = img.shape
    print((HEIGHT, WIDTH))

    alpha = {}
    for n in range(97, 122):
        alpha[chr(n)] = []

    original = Image.open('src/images/'+filename)

    for i in range(len(d['char'])):
        print(d['char'][i])
        print((d['left'][i], HEIGHT-d['top'][i]-1000, d['right'][i], HEIGHT-d['bottom'][i]-1000))

        os.mkdir('my_fonts/'+dir)
        if d['char'][i].isalpha():
            cropped = original.crop((d['left'][i], HEIGHT-d['top'][i]-1000, d['right'][i], HEIGHT-d['bottom'][i]-1000))
            alpha[d['char'][i].lower()].append(cropped)
            cropped.save('my_fonts/'+dir+'/'+d['char'][i].lower()+'.png', 'PNG')

    return alpha
