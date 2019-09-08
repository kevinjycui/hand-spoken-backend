from pytesseract import pytesseract as pt
import PIL
from PIL import Image
from pytesseract import Output
import cv2
import pprint
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import os

dev_user = input('Enter dev user for tesseract cmd ([s]teph, [k]evin):\n--> ').lower()
if dev_user == 'steph' or dev_user == 's':
    _c = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
elif dev_user == 'kevin' or dev_user == 'k':
    _c = r'C:\Users\kevin\AppData\Local\Tesseract-OCR\tesseract.exe'
pt.tesseract_cmd = _c

def processImage(filename):
    img = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2GRAY)
    # alpha = 2.5
    # beta = 70
    # for y in range(img.shape[0]):
    #     for x in range(img.shape[1]):
    #         for c in range(img.shape[2]):
    #             img[y,x,c] = np.clip(alpha*img[y,x,c] + beta, 0, 255)
    d = pt.image_to_boxes(img, output_type=Output.DICT)
    return d

def cropImages(filename, dir):
    d = processImage('src/images/'+filename)
    img = cv2.imread('src/images/'+filename)
    WIDTH, HEIGHT, _ = img.shape

    original = Image.open('src/images/'+filename)
    
    if not os.path.exists('my_fonts/'+dir):
        os.mkdir('my_fonts/'+dir)

    for i in range(len(d['char'])):
        print(d['char'][i])
        # print((d['left'][i], HEIGHT-d['top'][i]-1000, d['right'][i], HEIGHT-d['bottom'][i]-1000))
        if d['char'][i].isalpha():
            cropped = original.crop((d['left'][i], HEIGHT-d['top'][i]-1000, d['right'][i], HEIGHT-d['bottom'][i]-1000))
            # cv2.imwrite(d['char'] + '.png',img)
            fig = plt.figure(frameon=False)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            plt.imshow(cropped)
            plt.savefig('my_fonts/'+dir+'/'+str(d['char'][i]) + ".svg", bbox_inches='tight', pad_inches=0)
            plt.close(fig)
