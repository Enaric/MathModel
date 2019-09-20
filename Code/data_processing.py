# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import datetime

def delete(backward,forward):
    global d
    # TODO 删除[backward,forward]区间的数据，方法有问题
    d = np.delete(d, [backward, forward], axis=0)

def deleteBatch(i):
    global d
    forward = i
    backward = i
    while d['GPS车速'][forward] >= 10 and forward<d.shape[0]-1:
        # 非怠速
        forward += 1
    while d['GPS车速'][backward] >= 10 and backward > 1:
        # 非怠速
        backward -= 1
    delete(backward,forward)

def str_to_datetime(st):
    return datetime.datetime.strptime(st, "%Y/%m/%d %H:%M:%S")

# read csv
d = pd.read_csv('original_data/file1.csv')

# data processing

# 1 data transform --replace datatime to time series
d['时间'] = d['时间'].apply(lambda x: int((str_to_datetime(x.replace(".000.",""))-datetime.datetime(2017,12,18,13,42,12)).total_seconds()))

# 2 data processing
# TODO 重复值清洗

for i in range(d.shape[0]-1):
    # 2.1 时间不连续删除整个运动片段
    # if d['时间'][i+1]-d['时间'][i]>1:
    #     print("时间不连续异常" + str(i))
        # deleteBatch(i)
    # 2.2 加速度异常删除整个运动片段
    # if d['GPS车速'][i]>100:
    #     backward = i
    #     while d['GPS车速'][backward]>10 and backward>1:
    #         backward -= 1
    #     if i-backward < 7:
    #         print("加速度异常"+str(i))
            # deleteBatch(i)
    # 2.3长期停车/怠速(停车超过180秒)
    if d['GPS车速'][i] < 10:
        forward = i
        while d['GPS车速'][forward] < 10 and forward < d.shape[0]-1:
            forward += 1
        if(forward-i)>180:
            print("长期停车/怠速异常" + str(i))
            delete(i,forward-180)
print(d.shape)

# write csv
# d.to_csv('processed_data/file1.csv')



#line chart

