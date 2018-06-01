#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from case.base import base
import ddt,os,json
from config.read_excel import read_Excel
from common.CommonMethod import CommonMethod
from config.write_excel import write_excel
from config.get_parameters import get_parameters

'''从excel中获取参数'''
absolute_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TestDataFile=os.path.join(absolute_path,"testdata.xlsx")
print(TestDataFile)
sheetName = "Sheet1"
ParameterData = read_Excel(TestDataFile, sheetName)
testData = ParameterData.dict_data()
#print(ParameterData)
print(testData)
#testData=get_parameters().read_para("Sheet1")

'''ddt模式对接口进行获取参数驱动'''
@ddt.ddt
class LoginTest(base):
    path=CommonMethod().Get_Path("loginpath")

    def login(self,data):
        url = ''.join([self.host,data["path"]])

        AllDate={"headers": json.loads(self.headers),self.DataType: data}
        response = CommonMethod().Method(url,data["method"], **AllDate)
        print(response)

        try:
            self.assertIn(data["expectedResult"], response)    #因为此接口返回数据很少，所以断言是否包含
            self.logger.info("断言通过")
        except:
            self.logger.info("断言没有通过")
            raise
        response["rowNum"]=data["rowNum"]
        print(response)
        #CommonMethod().Write_Token(response["auth_token"])
        #super().wirte_result(response, TestDataFile, sheetName)

    @ddt.data(*testData)
    def test_login(self,data):
        print("当前测试数据%s" % data)
        self.login(data)



if __name__ == "__main__":
    unittest.main()

