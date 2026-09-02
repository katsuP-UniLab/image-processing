import cv2 as cv
import matplotlib.pyplot as plt

from src.modules.dirCheck import dirCheck

root = "src/assets/week_03/"


def exercise():
    img = cv.imread(root + "icon-200.png")
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # ponytail: cv.rotate handles 90/180/270; np.rot90 is an even lazier zero-copy one-liner
    rot_90 = cv.rotate(rgb_img, cv.ROTATE_90_CLOCKWISE)
    rot_180 = cv.rotate(rgb_img, cv.ROTATE_180)
    rot_270 = cv.rotate(rgb_img, cv.ROTATE_90_COUNTERCLOCKWISE)

    images = [
        ("Original", rgb_img),
        ("Rotate 90°", rot_90),
        ("Rotate 180°", rot_180),
        ("Rotate 270°", rot_270),
    ]

    plt.figure(figsize=(10, 3))
    for idx, (title, image) in enumerate(images, start=1):
        plt.subplot(1, 4, idx)
        plt.imshow(image)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    dirCheck(root)
    cv.imwrite(root + "out/rot_90.png", cv.rotate(img, cv.ROTATE_90_CLOCKWISE))
    cv.imwrite(root + "out/rot_180.png", cv.rotate(img, cv.ROTATE_180))
    cv.imwrite(root + "out/rot_270.png", cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE))
