import cv2 as cv
import matplotlib.pyplot as plt

from src.modules.dirCheck import dirCheck

root = 'src/assets/week_03/'

def exercise ():
    img = cv.imread(root + 'icon-200.png')
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    threshold_value = 128
    ret, thresholded_img = cv.threshold(grey_img, threshold_value, 255, cv.THRESH_BINARY)

    plt.figure(figsize=(8,4))

    plt.subplot(2,4,1)
    plt.imshow(rgb_img)
    plt.title('original')
    plt.axis('off')

    plt.subplot(2,4,2)
    ret, thresholded_img = cv.threshold(grey_img, 128, 255, cv.THRESH_BINARY)
    plt.imshow(thresholded_img, cmap='gray')
    plt.title('threshold = 128')
    plt.axis('off')

    plt.subplot(1,4,1)
    ret, thresholded_img = cv.threshold(grey_img, 50, 255, cv.THRESH_BINARY)
    plt.imshow(thresholded_img, cmap='gray')
    plt.title('threshold = 50')
    plt.axis('off')

    plt.subplot(1,4,2)
    ret, thresholded_img = cv.threshold(grey_img, 100, 255, cv.THRESH_BINARY)
    plt.imshow(thresholded_img, cmap='gray')
    plt.title('threshold = 100')
    plt.axis('off')


    plt.subplot(1,4,3)
    ret, thresholded_img = cv.threshold(grey_img, 200, 255, cv.THRESH_BINARY)
    plt.imshow(thresholded_img, cmap='gray')
    plt.title('threshold = 200')
    plt.axis('off')

    plt.show()

