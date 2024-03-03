#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import barcode
from barcode.writer import ImageWriter
from barcode_data import barcodeData
from make_pdf import MakePdf
from make_pdf_customer import MakePdfCustomer
from customer_data import customerData

OUTPUT_PIC_DIR = "output_pic"
OUTPUT_PDF_FILE = "output_pdf/output.pdf"

OUTPUT_PIC_DIR_CUSTOMER = "output_pic_customer"
OUTPUT_PDF_FILE_CUSTOMER = "output_pdf/output_customer.pdf"

def main():
    # 商品JAN出力
    output_jan_pdf()
    output_customer_pdf()

def output_jan_pdf():
    # 商品JAN出力
    data = []

    # csvの読み込み
    with open('barcode_base.csv', "r",encoding="UTF-8") as f:

        # csvから内容を一括で取り出す
        reader = csv.reader(f)

        # 1行ずつ取り出す
        for row in reader:
            barcode_path = f"{OUTPUT_PIC_DIR}/{row[0]}.png"
            product_id = row[0]
            product_name = row[1]
            jan_code = row[2]

            # JANコード画像の生成
            jan = barcode.get('jan', jan_code, writer=ImageWriter())
            # JANコード画像の保存
            jan.save(f"{OUTPUT_PIC_DIR}/{row[0]}",options={
                'font_size':12,
                'text_distance':5,
                'font_path':'./OCRB.TTF',
                'quiet_zone':2,
                })
            data.append(barcodeData(barcode_path,product_id, product_name))

    # データの表示
    for d in data:
        print(d.barcode_path,d.product_id, d.product_name)

    # PDF出力
    pdf_maker = MakePdf(OUTPUT_PDF_FILE, data)
    pdf_maker.make_pdf()

def output_customer_pdf():
    data = []

    # csvの読み込み
    with open('customer_base.csv', "r",encoding="UTF-8") as f:

        # csvから内容を一括で取り出す
        reader = csv.reader(f)

        # 1行ずつ取り出す
        for row in reader:
            barcode_path = f"{OUTPUT_PIC_DIR_CUSTOMER}/{row[0]}.png"
            customer_no = row[0]
            customer_name = row[1]

            # コード画像の生成
            customer = barcode.get('nw-7', customer_no, writer=ImageWriter())
            # JANコード画像の保存
            customer.save(f"{OUTPUT_PIC_DIR_CUSTOMER}/{row[0]}",options={
                'font_size':12,
                'text_distance':5,
                'font_path':'./OCRB.TTF',
                'quiet_zone':2,
                })
            data.append(customerData(barcode_path,customer_no, customer_name))

    # データの表示
    for d in data:
        print(d.barcode_path,d.customer_no, d.customer_name)

    # PDF出力
    pdf_maker = MakePdfCustomer(OUTPUT_PDF_FILE_CUSTOMER, data)
    pdf_maker.make_pdf()


if __name__ == "__main__":
    main()
