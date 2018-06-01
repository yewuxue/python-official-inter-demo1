#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import unittest
from case.base import base
import ddt,json
from common.CommonMethod import CommonMethod
from config.get_parameters import get_parameters

#testData=get_parameters().read_para("Sheet1")
Sheet="Sheet1"
'''ddt模式对接口进行获取参数驱动'''
@ddt.ddt
class LoginTest(base):
    testData = get_parameters().read_para(Sheet)
    @ddt.data(*testData)
    def test_login(self,data):

        self.logger.info("当前测试数据%s" % data)
        url = ''.join([self.host,data["path"]])
        AllDate = {"headers": json.loads(self.headers), self.DataType: data}
        response = CommonMethod().Method(url,data["method"], **AllDate)
        print(response)
        try:
            self.assertIn(data["expectedResult"], response)  # 因为此接口返回数据很少，所以断言是否包含
            self.logger.info("断言通过")
        except:
            self.logger.error("断言没有通过")
            raise

        response["rowNum"] = data["rowNum"]
        CommonMethod().Write_Token(response["auth_token"])

        super().wirte_result(response,Sheet)



if __name__ == "__main__":
    unittest.main()

