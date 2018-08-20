# -*- coding: utf-8 -*-
'''
分析输入的CSV文件，生成腐蚀监测数据分析结果
20,SN:1600001,Tag NO:RE-0001,0.504mm
1,2017,2,15,8,0,50000,50000
2,2017,2,15,10,0,49900,50000
CSV文件格式如上所示
'''


def getData(fileName):
    '''输入文件名，返回时间，测试电阻，参考电阻'''

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
        li1,li2,li3,li4,li5,li6,li7,li8 = line.split(',')
        times.append(str(li2+li3+li4+li5+li6))
        resElements.append(float(li7))
        resRefers.append(float(li8))
    dataFile.close()
    return (times,resElements,resRefers)


if __name__ == "__main__":
    print(getData('D:\code\SLasH\ER-0001.csv'))
    
