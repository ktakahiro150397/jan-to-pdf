from typing import List
from customer_data import customerData
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BARCODE_VERTICAL_INITIAL = 750
BARCODE_VERTICAL_DIFF = 150
BARCODE_CHANGE_DATA_COUNT = 5
BARCODE_FIRST_COLUMN_X = 50
BARCODE_SECOND_COLUMN_X = 350

class MakePdfCustomer:
    def __init__(self, file_path, customer_data: List[customerData]):
        self.file_path = file_path
        self.customer_data = customer_data

    def make_pdf(self):
        page = canvas.Canvas(self.file_path,pagesize=portrait(A4))

        # フォントの設定
        pdfmetrics.registerFont(TTFont('meiryo', 'Meiryo.ttf'))
        page.setFont('meiryo', 12)

        # 10個ずつバーコードを描画
        for page_num, data in enumerate(self.split_list(self.customer_data,10)):
            self.draw_barcode_list(page,page_num,data)
            page.showPage()
        
        page.save()

        print(f"Output PDF to {self.file_path}")
    
    def draw_barcode_list(self,page:canvas.Canvas,page_num:int,customer_data:List[customerData]):
        page.setFont('meiryo', 12)
        page.drawString(50, 800, f"顧客情報 {page_num+1}ページ")
        
        for i, data in enumerate(customer_data):
            # 列位置
            if i <= BARCODE_CHANGE_DATA_COUNT - 1:
                position_x = BARCODE_FIRST_COLUMN_X
            else:
                position_x = BARCODE_SECOND_COLUMN_X
            
            # 行位置
            if i <= BARCODE_CHANGE_DATA_COUNT - 1:
                position_y = BARCODE_VERTICAL_INITIAL - i * BARCODE_VERTICAL_DIFF
            else:
                position_y = BARCODE_VERTICAL_INITIAL - (i - BARCODE_CHANGE_DATA_COUNT) * BARCODE_VERTICAL_DIFF

            self.draw_barcode(page,data,position_x,position_y)
            print(f"index:{i} Output {data.customer_name} to PDF ({position_x},{position_y})")

    def draw_barcode(self,page:canvas.Canvas,customer_data:customerData,position_x,position_y):
        font_size = 12
        page.setFont('meiryo', font_size)

        page.drawString(x=position_x,y=position_y,text=customer_data.customer_no)
        page.drawString(x=position_x,y=position_y-font_size*1.2,text=customer_data.customer_name)
        page.drawImage(customer_data.barcode_path,position_x,position_y-font_size*1.2-105,
                       width=200,height=100)
        
    def split_list(self,customer_data:List[customerData],n:int):
        for idx in range(0,len(customer_data),n):
            yield customer_data[idx:idx+n]
            