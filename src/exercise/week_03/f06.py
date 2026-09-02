import cv2 as cv
import matplotlib.pyplot as plt

from src.modules.dirCheck import dirCheck

root = "src/assets/week_03/"


def exercise():
    # 1. อ่านภาพ
    img = cv.imread(root + "icon-200.png")
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # 2. แปลงเป็น Grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 3 & 4. ใช้ Canny Edge Detection และทดลองค่า Threshold ต่าง ๆ
    # ponytail: list comprehension over threshold pairs avoids repetitive Canny calls & subplot boilerplate
    thresholds = [(50, 150), (100, 200), (150, 250)]
    results = [("Original", rgb_img, None)] + [
        (f"Canny ({t1}, {t2})", cv.Canny(gray_img, t1, t2), "gray")
        for t1, t2 in thresholds
    ]

    # 5. เปรียบเทียบผลลัพธ์
    plt.figure(figsize=(12, 3))
    for idx, (title, image, cmap) in enumerate(results, start=1):
        plt.subplot(1, 4, idx)
        plt.imshow(image, cmap=cmap)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    dirCheck(root)
    for t1, t2 in thresholds:
        cv.imwrite(root + f"out/canny_{t1}_{t2}.png", cv.Canny(gray_img, t1, t2))
