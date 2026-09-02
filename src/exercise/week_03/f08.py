import cv2 as cv
import matplotlib.pyplot as plt

from src.modules.dirCheck import dirCheck

root = "src/assets/week_03/"


def exercise():
    # 1. อ่านภาพ
    img = cv.imread(root + "icon-200.png")
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # 2, 3, 4. แยกสี Red, Green, Blue (OpenCV อ่านภาพในรูปแบบ BGR)
    # ponytail: cv.split(img) is native OpenCV; b, g, r = [img[:, :, i] for i in range(3)] is direct numpy indexing
    b, g, r = cv.split(img)

    # 5. แสดงผลเปรียบเทียบ
    channels = [
        ("Original", rgb_img, None),
        ("Red Channel", r, "gray"),
        ("Green Channel", g, "gray"),
        ("Blue Channel", b, "gray"),
    ]

    plt.figure(figsize=(12, 3))
    for idx, (title, image, cmap) in enumerate(channels, start=1):
        plt.subplot(1, 4, idx)
        plt.imshow(image, cmap=cmap)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    dirCheck(root)
    cv.imwrite(root + "out/red_channel.png", r)
    cv.imwrite(root + "out/green_channel.png", g)
    cv.imwrite(root + "out/blue_channel.png", b)
