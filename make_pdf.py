from typing import List
from barcode_data import barcodeData
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BARCODE_VERTICAL_INITIAL = 750
BARCODE_VERTICAL_DIFF = 150
BARCODE_CHANGE_DATA_COUNT = 5
BARCODE_FIRST_COLUMN_X = 50
BARCODE_SECOND_COLUMN_X = 350

class MakePdf:
    def __init__(self, file_path, barcode_data: List[barcodeData]):
        self.file_path = file_path
        self.barcode_data = barcode_data

    def make_pdf(self):
        page = canvas.Canvas(self.file_path,pagesize=portrait(A4))

        # フォントの設定
        pdfmetrics.registerFont(TTFont('segoe', 'segoe-ui.ttf'))
        pdfmetrics.registerFont(TTFont('meiryo', 'Meiryo.ttf'))
        page.setFont('meiryo', 12)

        # page.drawString(50, 800, "JANコード一覧")

        # 10個ずつバーコードを描画
        for page_num, data in enumerate(self.split_list(self.barcode_data,10)):
            self.draw_barcode_list(page,page_num,data)
            page.showPage()
        
        page.save()

        print(f"Output PDF to {self.file_path}")
    
    def draw_barcode_list(self,page:canvas.Canvas,page_num:int,barcode_data:List[barcodeData]):
        page.setFont('meiryo', 12)
        page.drawString(50, 800, f"JANコード一覧 {page_num+1}ページ")
        
        for i, data in enumerate(barcode_data):
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
            print(f"index:{i} Output {data.product_name} to PDF ({position_x},{position_y})")

    def draw_barcode(self,page:canvas.Canvas,barcode_data:barcodeData,position_x,position_y):
        font_size = 12
        page.setFont('meiryo', font_size)

        page.drawString(x=position_x,y=position_y,text=barcode_data.product_id)
        page.drawString(x=position_x,y=position_y-font_size*1.2,text=barcode_data.product_name)
        page.drawImage(barcode_data.barcode_path,position_x,position_y-font_size*1.2-105,
                       width=200,height=100)
        
    def split_list(self,barcode_data:List[barcodeData],n:int):
        for idx in range(0,len(barcode_data),n):
            yield barcode_data[idx:idx+n]