import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from src.modules.dirCheck import dirCheck

root = "src/assets/week_03/"


def exercise():
    # 1. อ่านภาพ
    img = cv.imread(root + "icon-200.png")

    # 2. วาดเส้นตรง (Line)
    cv.line(img, (10, 15), (190, 15), (0, 255, 0), 2)

    # 3. วาดสี่เหลี่ยม (Rectangle)
    cv.rectangle(img, (20, 25), (180, 165), (255, 0, 0), 2)

    # 4. วาดวงกลม (Circle)
    cv.circle(img, (100, 95), 35, (0, 165, 255), 2)

    # 5. เพิ่มข้อความชื่อนักศึกษา
    # ponytail: cv.putText is the OpenCV ASCII standard; PIL is used here for true Thai font rendering
    try:
        pil_img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_img)
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Thonburi.ttc", 14)
        draw.text((25, 172), "ศุภกฤต ภิญโญวรพจน์", font=font, fill=(0, 0, 255))
        img = cv.cvtColor(np.array(pil_img), cv.COLOR_RGB2BGR)
    except Exception:
        # Fallback to OpenCV cv.putText
        cv.putText(
            img,
            "Suphakrit Phinyoworaphot",
            (10, 185),
            cv.FONT_HERSHEY_SIMPLEX,
            0.4,
            (0, 0, 255),
            1,
            cv.LINE_AA,
        )

    cv.imshow("Exercise 07 - Shapes & Text", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    dirCheck(root)
    cv.imwrite(root + "out/annotated_image.png", img)
