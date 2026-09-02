import cv2 as cv

from src.modules.dirCheck import dirCheck

root = "src/assets/week_03/"


def exercise():
    img = cv.imread(root + "icon-200.png")

    # Resize to 50%
    resize_50 = cv.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

    # Resize to 200%
    resize_200 = cv.resize(img, (0, 0), fx=2.0, fy=2.0, interpolation=cv.INTER_CUBIC)

    # Display images with cv.imshow
    cv.imshow("Original", img)
    cv.imshow("Resize 50%", resize_50)
    cv.imshow("Resize 200%", resize_200)

    cv.waitKey(0)
    cv.destroyAllWindows()

    dirCheck(root)
    cv.imwrite(root + "out/resize_50.png", resize_50)
    cv.imwrite(root + "out/resize_200.png", resize_200)
