#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import logging

class logger1():
    def logging(logFilePath="test.log",level=logging.DEBUG):
        logging.basicConfig(level=level)
        #定义一个SreamHandler
        Rtandler=logging.handlers.RotatingFileHandler(logFilePath,maxBytes=10*1024*1024,backupCount=5)
        Rtandler.setLevel(level)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")
        Rtandler.setFormatter(fmt)
        logging.getLogger("").addHandler(Rtandler)

if __name__=="__main__":
    pass