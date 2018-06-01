#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import os

from common.RequestsMethod import RequestsMethod
from config.ReadWriteConfigIni import readConfig

#filename="D:\pycharmworkspace\demo1\config\config.ini"

absolute_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filename=os.path.join(absolute_path,"config","config.ini")
print(filename)
class CommonMethod():
    # def read_configuration_file(self):
    #     '''获取配置文件的路径'''
    #     file_path = os.path.split(os.path.realpath(__file__))[0]
    #     read_config = readConfig(os.path.join(file_path, "config.ini"))
    #     return read_config
    def read_configuration_file(self):
        '''因为run_allcase_report.py运行时会在自己所在的目录去寻找，导致路径会丢失demo，所以目前先这样，后续会考虑从ini文件中读取，或者别的解决方式'''
        #file_path = os.path.split(os.path.realpath(__file__))[0]
        read_config = readConfig(filename)
        return read_config



    def Get_Host(self):
        '''获取服务器地址'''
        read_config=self.read_configuration_file()
        vaule=read_config.getConfigVaule("Host","host")
        return vaule

    def Get_Port(self):
        '''获取端口的方法'''
        read_config = self.read_configuration_file()
        vaule = read_config.getConfigVaule("UrlPort", "port")
        return vaule

    def Get_Path(self,path):
        '''获取接口路径的方法'''
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("Path", path)
        return vaule

    def Get_Headers(self):
        '''获取请求头的方法'''
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("Headers", "headers")
        return vaule

    def Write_Token(self,vaule):
        readConfig(filename).writeConfig("Headers","token",vaule,filename)

    def Get_Token(self):
        '''获取请求头的方法'''
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("Headers", "token")
        return vaule

    def Get_Method(self):
        '''获取请求方法的方法'''
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("Method", "method")
        return vaule

    def Get_DataType(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DataType", "dataType")
        return vaule

    def Get_ServerHost(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBHost", "serverHost")
        return vaule

    def Get_DbHost(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBHost", "dbHost")
        return vaule

    def Get_ServerPort(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBPort", "serverPort")
        return vaule

    def Get_DbPort(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBPort", "dbPort")
        return vaule

    def Get_ServerUser(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBUser", "serverUser")
        return vaule

    def Get_DbUser(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBUser", "dbUser")
        return vaule

    def Get_ServerPassword(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBPassWord", "serverPassword")
        return vaule

    def Get_DbPassword(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBPassWord", "dbPassword")
        return vaule

    def Get_DBName(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("DBName", "name")
        return vaule

    def Get_DBEncoding(self):
        file = self.read_configuration_file()
        vaule = file.getConfigVaule("Encoding", "charset")
        return vaule

    def Method(self,url,Method,**AllData):
        '''判断请求是什么方法'''
        global res
        if Method == "get":
            res=RequestsMethod().Get_Method(url,**AllData)
        elif Method == "post":
            res=RequestsMethod().Post_Method(url,**AllData)
        return res

if __name__ == "__main__":
    '''调试'''
    b ={"X-Auth-Token"     :        CommonMethod().Get_Token()}
    print(b)
