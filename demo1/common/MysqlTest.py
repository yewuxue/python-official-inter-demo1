#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from common.CommonMethod import CommonMethod
import os,pymysql
from sshtunnel import SSHTunnelForwarder


private_key_file=os.path.join(os.path.split(os.path.dirname(os.path.realpath(__file__)))[0],"config","id_rsa")
class MysqlTest():
    def __init__(self):
        #private_key_file = os.path.expanduser(r"C:\Users\Administrator\.ssh\id_rsa")
        self.ServerHost=CommonMethod().Get_ServerHost()
        self.ServerPort=eval(CommonMethod().Get_ServerPort())
        self.ServerUser=CommonMethod().Get_ServerUser()
        self.DbHost=CommonMethod().Get_DbHost()
        self.DbPort=eval(CommonMethod().Get_DbPort())
        self.DbUser=CommonMethod().Get_DbUser()
        self.DbPassword=CommonMethod().Get_DbPassword()
        self.DbName=CommonMethod().Get_DBName()
        self.Charset=CommonMethod().Get_DBEncoding()
    def connectMysql(self,sql):
        with SSHTunnelForwarder((self.ServerHost,self.ServerPort),
                ssh_username=self.ServerUser,
                ssh_pkey=private_key_file,
                remote_bind_address=(self.DbHost,self.DbPort)) as tunnel:

            conn = pymysql.connect(host='127.0.0.1', user=self.DbUser,
                    passwd=self.DbPassword, db=self.DbName,
                    charset=self.Charset,
                    port=tunnel.local_bind_port)


            cursor = conn.cursor()
            cursor.execute(sql)
            for single_information in cursor.fetchall():
                print(single_information)
                #return single_information
            conn.commit()
            conn.close()

if __name__ =="__main__":
    sql="SELECT * FROM `st_employee` WHERE `store_id` LIKE '%180631%' AND `brand_id` = '116126' LIMIT 0, 1000"
    #sql="INSERT INTO risk_data (store_st_id,brand_st_id,is_club,`date`,employee_count,coach_count) VALUES ('180631','116126','1','2018-05-18','3','1')"
    MysqlTest().connectMysql(sql)