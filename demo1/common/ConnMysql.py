#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import pymysql
from common.CommonMethod import CommonMethod
class connectMysql():
    def __init__(self):
        sql_conn_dict = {
            "host":CommonMethod().Get_DBHost(),
            "port":eval(CommonMethod().Get_DBPort()),
            "user":CommonMethod().Get_DBUser(),
            "passwd":CommonMethod().Get_DBPassWord(),
            "db":CommonMethod().Get_DBName(),
            "charset":CommonMethod().Get_DBEncoding()
        }
        # 1.创建链接
        self.conn = pymysql.connect(**sql_conn_dict)
        # 2.获取游标
        self.cur =self.conn.cursor()

    def SelectOperation(self,sql):
        '''查询数据库操作'''
        #sql = "select * from user"
        self.cur.execute(sql)
        return self.cur.fetchmany()

    def UpdateOperation(self):
        '''更新数据库操作'''
        pass

    def DeleteOperation(self):
        '''删除数据库操作'''
        pass

    def InsertOperation(self):
        '''插入数据库操作'''
        pass

    def closeMysql(self):
        # 4.关闭游标，数据库链接
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    '''还需要改进'''
    sql = "select * from user"
    conn=connectMysql()
    a=conn.SelectOperation(sql)
    print(a)
    conn.closeMysql()
