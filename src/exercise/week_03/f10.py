import cv2 as cv
import matplotlib.pyplot as plt

from src.modules.dirCheck import dirCheck

root = "src/assets/week_03/"


def exercise():
    # 1. โหลดภาพจากไฟล์
    img = cv.imread(root + "icon-200.png")
    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # 3. แปลงเป็น Grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 4. แปลงเป็น Binary
    _, binary_img = cv.threshold(gray_img, 128, 255, cv.THRESH_BINARY)

    # 5. ตรวจจับขอบภาพ (Canny)
    edges_img = cv.Canny(gray_img, 100, 200)

    # ponytail: looping over pipeline stages unifies matplotlib display and file saving
    stages = [
        ("Original", rgb_img, img, None),
        ("Grayscale", gray_img, gray_img, "gray"),
        ("Binary", binary_img, binary_img, "gray"),
        ("Edges", edges_img, edges_img, "gray"),
    ]

    # 2 & 5. แสดงผลเปรียบเทียบทุกขั้นตอน
    plt.figure(figsize=(12, 3))
    for idx, (title, show_img, _, cmap) in enumerate(stages, start=1):
        plt.subplot(1, 4, idx)
        plt.imshow(show_img, cmap=cmap)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    # 6. บันทึกผลลัพธ์ทั้งหมด
    dirCheck(root)
    for title, _, save_img, _ in stages:
        cv.imwrite(f"{root}out/{title.lower()}.png", save_img)
