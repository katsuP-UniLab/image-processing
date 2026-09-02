import cv2 as cv

from src.modules.dirCheck import dirCheck

root = 'src/assets/week_03/'

def example ():
    img = cv.imread(root + 'katchan-crop.jpeg')

    if img is None: 
        print('Image not found.. Please try again..')
    else:
        print('Image Found')

        grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # cv.imshow('Image', img)
        cv.imshow('Grey image', grey_img)

        dirCheck(root)
        
        # Save Image
        cv.imwrite(root + 'out/katchan.jpeg', img)
        cv.imwrite(root + 'out/kat-grey.jpeg', grey_img)

        cv.waitKey(0)
        cv.destroyAllWindows()

        print('Image saved..')
