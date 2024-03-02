from typing import List
from barcode_data import barcodeData

class MakePdf:
    def __init__(self, file_path, barcode_data: List[barcodeData]):
        self.file_path = file_path
        self.barcode_data = barcode_data

    def make_pdf(self):
        

        print(f"Making PDF from {self.file_path}")