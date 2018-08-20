# -*- coding: utf-8 -*-
'''
分析输入的CSV文件，生成腐蚀监测数据分析结果
'''


def getData(fileName):
    '''输入文件名，返回时间，测试电阻，参考电阻'''
    dataFile = open(fileName, 'r')
