#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from case.base import base
import ddt,json
from common.CommonMethod import CommonMethod
from config.get_parameters import get_parameters

testData=get_parameters().read_para("Sheet2")


'''ddt模式对接口进行获取参数驱动'''
@ddt.ddt
class query_stores(base):

    @ddt.data(*testData)
    def test_query_stores(self,data):
        self.logger.info("当前测试数据%s" % data)
        url = ''.join([self.host,data["path"]])
        AllDate = {"headers": json.loads(self.headers), self.DataType: data}
        print(AllDate)
        response = CommonMethod().Method(url,data["method"], **AllDate)
        print(response)





if __name__ == "__main__":
    unittest.main()

