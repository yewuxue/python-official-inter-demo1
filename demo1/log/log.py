#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import logging

class logger():
    def __init__(self,consoleLevel,logFile,fileLevel):
    #def __init__(self,consoleLevel, logFile, fileLevel):
        #创建logger对象
        self.logger=logging.getLogger("测试日志")
        #设置默认log级别
        self.logger.setLevel(logging.DEBUG)
        #定义输出handler的格式
        fmt=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")

        if not self.logger.handlers:
            #设置控制台日志
            self.cg=logging.StreamHandler()
            #配置logger
            self.cg.setFormatter(fmt)
            self.cg.setLevel(consoleLevel)

            #设置文件日志

            self.fg=logging.FileHandler(logFile,"a",encoding="utf-8")
            self.fg.setFormatter(fmt)
            self.fg.setLevel(fileLevel)

            #给logger添加handler
            self.logger.addHandler(self.cg)
            self.logger.addHandler(self.fg)

    def debug(self,message):
        self.logger.debug(message)
        self.logger.removeHandler(self.logger.handlers)
    def info(self,message):
        self.logger.info(message)
        self.logger.removeHandler(self.logger.handlers)
    def warning(self,message):
        self.logger.warning(message)
        self.logger.removeHandler(self.logger.handlers)
    def error(self,message):
        self.logger.error(message)
        self.logger.removeHandler(self.logger.handlers)
    def critical(self,message):
        self.logger.critical(message)
        self.logger.removeHandler(self.logger.handlers)

if __name__=="__main__":
    logger=logger(consoleLevel=logging.INFO,logFile="logger.txt",fileLevel=logging.INFO)
    #应用日志
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning信息')
    logger.error('error')
    logger.critical('critical')



