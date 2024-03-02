from typing import List

from barcode_data import barcodeData
class MakePdf:
    def __init__(self, file_path, barcodeData: List[barcodeData]):
        self.file_path = file_path
        self.barcodeData = barcodeData

    def make_pdf(self):
        print(f"Making PDF from {self.file_path}")