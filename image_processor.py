# import pytesseract
from pytesseract import pytesseract as pt
import PIL
from PIL import Image
from pytesseract import Output
import cv2
import pprint
import matplotlib
from matplotlib import pyplot as plt

pt.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def processImage(filename):
    img = cv2.imread(filename)
    d = pt.image_to_boxes(img, output_type=Output.DICT)
    return d

def cropImages(filename):
    d = processImage(filename)
    img = cv2.imread(filename)
    WIDTH, HEIGHT, _ = img.shape
    print((HEIGHT, WIDTH))

    alpha = {}
    for n in range(97, 123):
        alpha[chr(n)] = []

    original = Image.open(filename)

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
            plt.savefig(str(d['char'][i]) + ".svg", bbox_inches='tight', pad_inches=0)
            plt.close(fig)
            
    return alpha

cropImages('text-jennifer.jpg')

# crop_img = img[d['top'][1]:d['bottom'][1], d['right'][1]:d['left'][1]]
# cv2.imshow("cropped", crop_img)
# n_boxes = len(d['char'])
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['bottom'][i], d['right'][i], d['top'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# img = cv2.imread('bw.png')
# for b in d:
#     img = cv2.rectangle(img,(int(b[1]),h-int(b[2])),(int(b[3]),h-int(b[4])),(255,0,0),2)
# for b in d.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
# cv2.imshow('output',img)
# cv2.namedWindow("Display 1", flags=cv2.WINDOW_NORMAL)
# cv2.imshow("Display 1", img)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# original = Image.open(image_file)
# # cropped = original.crop((10,100,500,300))
# cropped = original.crop((d['left'][1], d['top'][1], 100, d['bottom'][1]))
# cropped.show()
