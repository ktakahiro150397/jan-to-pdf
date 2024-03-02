#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv,barcode
from barcode_data import barcodeData
from barcode.writer import ImageWriter

output_pic_dir = "output_pic"


def main():

    data = []

    # csvの読み込み
    with open(u'barcode_base.csv', "r") as f:

        # csvから内容を一括で取り出す
        reader = csv.reader(f)

        # 1行ずつ取り出す
        for row in reader:
            barcode_path = f"{output_pic_dir}/{row[0]}.png"
            product_name = row[1]

            # JANコード画像の生成
            jan = barcode.get('jan', product_name, writer=ImageWriter())
            # JANコード画像の保存
            filename = jan.save(f"{output_pic_dir}/{row[0]}",options={
                #'module_height':37.29,
                #'module_width':25.93,
                'quiet_zone':2,
                #'font_size':40,
                #'text_distance':5,
                #'font_path':'C:\\users\\hogehoge\\appdata\\local\\microsoft\\windows\\fonts\\ocrb.ttf'
                })
            data.append(barcodeData(barcode_path, product_name))

    # データの表示
    for d in data:
        print(d.barcode_path, d.product_name)

if __name__ == "__main__":
    main()