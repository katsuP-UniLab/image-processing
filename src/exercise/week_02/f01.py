def exercise ():
    total = int(input("ยอดซื้อสินค้า : "))

    new_total = 0

    if total >= 10000:
        new_total = total * (90 / 100)
    elif total >= 7000:
        new_total = total * (93 / 100)
    elif total >= 5000:
        new_total = total * (95 / 100)
    else:
        new_total = total

    print('')
    print('----------------------------------------------------')
    print('ราคาสินค้าทั้งหมด: ', total, ' บาท')
    print('ได้รับส่วนลด: ', total - new_total, ' บาท')
    print('จำนวนเงินที่ต้องจ่าย: ', new_total, ' บาท')
    print('----------------------------------------------------')
    print('')
