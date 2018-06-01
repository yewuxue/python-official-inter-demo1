#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from case.Test_a_Login import LoginTest
from case.Test_b_Query_stores import query_stores
import unittest


#运行部分测试用例方式1
# suite = unittest.TestSuite()
# suite.addTest(LoginTest("test_login"))
# suite.addTest(query_stores("test_query_stores"))
# if __name__=="__main__":
#     runner=unittest.TextTestRunner()
#     runner.run(suite)

    # # 运行部分测试用例方式2
    # tests=[stringTest("test01"),stringTest("test02")]
    # suite.addTests(tests)
    #
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    #
    #
    # #运行全部测试用例
    # allSuite=unittest.makeSuite(stringTest,"test")
    #
    # runner=unittest.TextTestRunner(verbosity=2)         #verbosity设置值后会显示出很多运行信息
    # runner.run(allSuite)

