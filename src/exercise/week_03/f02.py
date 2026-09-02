import cv2 as cv

from src.modules.dirCheck import dirCheck

root = 'src/assets/week_03/'

def exercise ():
    img = cv.imread(root + 'icon-200.png')
    grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('image', img)
    cv.imshow('grey image', grey_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

    dirCheck(root)
    cv.imwrite(root + 'out/grey_image.jpg', grey_img)

