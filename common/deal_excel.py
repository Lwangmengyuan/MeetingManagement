# coding: utf-8
from openpyxl import load_workbook
from common.setting import Settings


class DealExcel:
    def __init__(self):
        self.ws = None

    # def read_excel(self, *position):
    #     path = '../data/case.xlsx'
    #     wb = load_workbook(path)
    #     ws = wb['testcase']
    #     data_list = []
    #     for i in position:
    #         data_list.append(eval(ws[i].value))
    #     wb.close()
    #     return data_list

    s = Settings()

    def read(self, sheetname=None):
        path = self.s.excel_path
        wb = load_workbook(path)
        if sheetname:
            sheet = wb[sheetname]
        else:
            sheet = wb.active
        row = sheet.max_row
        column = self.s.excel_data_column
        data_list = []
        for r in range(2, row + 1):
            value = sheet.cell(r, column).value
            if value:
                data_list.append([eval(value)])
        wb.close()
        return data_list
