import cv2 as cv
import matplotlib.pyplot as plt

from src.modules.dirCheck import dirCheck

root = 'src/assets/week_03/'

def example ():
    img = cv.imread(root + 'katchan-crop.jpeg')

    if img is None: 
        print('Image not found.. Please try again..')
    else:
        print('Image Found')

        rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        plt.figure(figsize=(8,4))

        plt.subplot(1,2,1)
        plt.imshow(rgb_img)
        plt.title('original')
        plt.axis('off')

        plt.subplot(1,2,2)
        plt.imshow(grey_img, cmap='gray')
        plt.title('grayscale')
        plt.axis('off')

        plt.show()