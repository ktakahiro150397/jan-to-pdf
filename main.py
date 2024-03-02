#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import barcode
from barcode.writer import ImageWriter
from barcode_data import barcodeData
from make_pdf import MakePdf

OUTPUT_PIC_DIR = "output_pic"
OUTPUT_PDF_FILE = "output_pdf/output.pdf"

def main():

    data = []

    # csvの読み込み
    with open('barcode_base.csv', "r",encoding="UTF-8") as f:

        # csvから内容を一括で取り出す
        reader = csv.reader(f)

        # 1行ずつ取り出す
        for row in reader:
            barcode_path = f"{OUTPUT_PIC_DIR}/{row[0]}.png"
            product_name = row[0]
            jan_code = row[1]

            # JANコード画像の生成
            jan = barcode.get('jan', jan_code, writer=ImageWriter())
            # JANコード画像の保存
            jan.save(f"{OUTPUT_PIC_DIR}/{row[0]}",options={
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

    # PDF出力
    pdf_maker = MakePdf(OUTPUT_PDF_FILE, data)
    pdf_maker.make_pdf()

if __name__ == "__main__":
    main()
