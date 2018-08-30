# -*- coding: utf-8 -*-
# @Time    : 2018/08/20
# @Author  : DongFJ
# @Email   : sjsgydfj@163.com
# @File    : probe.py
# @Software: VS Code 1.26.1
'''
Description : 分析输入的CSV文件，图表呈现
主要内容：

20,SN:1600001,Tag NO:RE-0001,0.504mm
1,2017,2,15,8,0,50000,50000
2,2017,2,15,10,0,49900,50000
CSV文件格式如上所示
现在这个程序运行速度很慢，不知道什么原因
无论如何每天也得保持更新
Ti8后遗症太强了
'''
from datetime import datetime
import pprint
import pylab
import sqlite3


def getData(fileName):
    '''输入文件名，返回时间，测试电阻，参考电阻3个列表'''

    dataFile = open(fileName, 'r')
    times = []
    resElements = []
    resRefers = []
    li1 = []
    li2 = []
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    li7 = []
    li8 = []
    dataFile.readline()  # ignore header
    for line in dataFile:
        li1, li2, li3, li4, li5, li6, li7, li8 = line.split(',')
        times.append(str(li2 + '-' + li3 + '-' + li4 +
                         ' ' + li5 + ':' + li6 + ':' + '0'))
        resElements.append(float(li7))
        resRefers.append(float(li8))
    dataFile.close()
    return (times, resElements, resRefers)


def calcData(inputFile, oriThick):
    '''输入文件名，返回时间序列，metal loss序列
    其中metal loss单位为mm'''
    timestamp = []
    resRatio = []
    metalloss = []
    times, resElements, resRefers = getData(inputFile)
    for time_str in times:
        time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        timestamp.append(time)
    for i in range(len(resElements)):
        ratio = resRefers[i] / resElements[i]
        resRatio.append(ratio)
    for i in range(len(resRatio)):
        lose = (oriThick - oriThick * resRatio[i])
        metalloss.append(lose)
    return (timestamp, metalloss)


def plotData(inputFile, oriThick):
    timestamp, metalloss = calcData(inputFile, oriThick)
    timestamp = pylab.array(timestamp)
    metalloss = pylab.array(metalloss)
    # pylab.date2num(date),将date 类型转换为pylab的时间类型，
    # 使用pylab.plot_date()画图
    pylab.plot_date(pylab.date2num(timestamp), metalloss, 'bo',
                    label='Metal Loss(mm)')
    pylab.title('Metal Loss to Time')
    pylab.xlabel('Time')
    pylab.ylabel('Metal loss(mm)')
    pylab.show()


def creatDB():
    conn = sqlite3.connect('D:\code\SLasH\Probe.db')
    print('Open database successfully')
    c = conn.cursor()
    c.execute('''CREATE TABLE DATA
    (ID integer PRIMARY KEY autoincrement,
    TIME timestamp
    RESELM integer
    RESREF integer
    METALLOSS float)''')


if __name__ == "__main__":
    plotData('D:\code\SLasH\ER-0001.csv', 0.508)
    creatDB()
