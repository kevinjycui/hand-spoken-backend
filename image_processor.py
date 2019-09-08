from pytesseract import pytesseract as pt
import PIL
from PIL import Image
from pytesseract import Output
import cv2
import pprint
import matplotlib
from matplotlib import pyplot as plt
import os

pt.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

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
    for n in range(97, 123):
        alpha[chr(n)] = []

    original = Image.open('src/images/'+filename)
    
    os.mkdir('my_fonts/'+dir)

    for i in range(len(d['char'])):
        print(d['char'][i])
        # print((d['left'][i], HEIGHT-d['top'][i]-1000, d['right'][i], HEIGHT-d['bottom'][i]-1000))
        if d['char'][i].isalpha():
            cropped = original.crop((d['left'][i], HEIGHT-d['top'][i]-1000, d['right'][i], HEIGHT-d['bottom'][i]-1000))
            alpha[d['char'][i].lower()].append(cropped)
            # cv2.imwrite(d['char'] + '.png',img)
            fig = plt.figure(frameon=False)
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            plt.imshow(cropped)
            plt.savefig('my_fonts/'+dir+'/'+str(d['char'][i]) + ".svg", bbox_inches='tight', pad_inches=0)
            plt.close(fig)
            
    return alpha

