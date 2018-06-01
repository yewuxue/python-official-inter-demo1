#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
import urllib3
urllib3.disable_warnings()
class RequestsMethod():
    def Get_Method(self,url,**AllData):
        '''对get请求方法封装，**AllData是处理多个请求参数，所以需要是字典格式'''

        #字典通过key获取vaule
        json=AllData.get("json")
        headers=AllData.get("headers")
        data=AllData.get("data")
        params=AllData.get("params")

        r = requests.get(url=url, json=json, headers=headers,data=data,params=params,verify=False,allow_redirects=True)
        text=r.json()
        print(r.request.url)
        return text

    def Post_Method(self,url,**AllData):
        '''对post请求方法封装，**AllData是处理多个请求参数，所以需要是字典格式'''
        urllib3.disable_warnings()
        # 获取参数
        json=AllData.get("json")
        headers=AllData.get("headers")
        data=AllData.get("data")
        params=AllData.get("params")
        r = requests.post(url=url, json=json, headers=headers,data=data,params=params,verify=False,allow_redirects=True)
        #text=r.text
        text=r.json()
        print(r.request.url)
        return text



