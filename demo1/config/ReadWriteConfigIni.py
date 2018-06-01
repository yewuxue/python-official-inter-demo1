#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import configparser
class readConfig():
    def __init__(self,filename):
        self.config=configparser.ConfigParser()
        self.config.read(filename,encoding="utf-8")

    def getConfigVaule(self,section,option):
        '''获取配置文件vaule'''
        vaule=self.config.get(section,option)
        return vaule

    def writeConfig(self,section,option,vaule,filename):
        '''写入文件'''
        try:
            #self.config.add_section(section)  # 当存在时就不需要添加了，直接设置值即可
            self.config.set(section,option,vaule)
        except configparser.DuplicateSectionError:
            print("此section已存在！")
        self.config.write(open(filename, "w", encoding="utf-8"))

if __name__=="__main__":
    a=readConfig("config.ini")
    a.writeConfig("aaaa","bbbbb","ccccc","D:\pycharmworkspace\demo1\common\config.ini")