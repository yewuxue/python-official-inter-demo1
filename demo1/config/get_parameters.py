#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import os
from config.read_excel import read_Excel

class get_parameters():
    def read_para(self,sheetName):
        absolute_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        TestDataFile=os.path.join(absolute_path,"testdata.xlsx")
        ParameterData = read_Excel(TestDataFile, sheetName)
        testData = ParameterData.dict_data()
        return testData

if __name__=="__main__":
    a=get_parameters().read_para("Sheet1")
    print(a)