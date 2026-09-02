import cv2 as cv

from src.modules.dirCheck import dirCheck

root = 'src/assets/week_03/'

def exercise ():
    img = cv.imread(root + 'icon-200.png')

    height, width, channels = img.shape

    print(width, 'x', height)

    cv.imshow('image', img)

    cv.waitKey(0)
    cv.destroyAllWindows()

    dirCheck(root)
    cv.imwrite(root + 'out/copy_image.jpg', img)

