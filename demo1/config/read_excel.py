#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import xlrd
class read_Excel():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小亍 1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                s['rowNum'] = i + 2
                # 从第二行取对应 values 值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1

            return r
if __name__ == "__main__":
    filePath = r"D:\pycharmworkspace\demo1\testdata.xlsx"
    sheetName = "Sheet1"
    data = read_Excel(filePath, sheetName)
    testData=data.dict_data()
    #print(type(testData))
    print(testData)
    #print(testData[0]["username"])
    # print(data["password"])