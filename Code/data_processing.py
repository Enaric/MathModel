# -*- coding: utf-8 -*-

import pandas as pd
import datetime

# 用来记录脏数据区间
to_drop = []


# string转datatime
def str_to_datetime(st):
    return datetime.datetime.strptime(st, "%Y/%m/%d %H:%M:%S")


# read csv
d = pd.read_csv('original_data/file1.csv', usecols=['时间', 'GPS车速'])
print("Before data processing,data shape is:")
print(d.shape)

# data processing
print("Data processing...")
# 1 data transform --replace datatime to time series
d['时间'] = d['时间'].apply(lambda x: int(
    (str_to_datetime(x.replace(".000.", "")) - datetime.datetime(2017, 12, 18, 13, 42, 12)).total_seconds()))

# 2 data processing
# TODO 重复值清洗（没有发现）

i = 0
while i < d.shape[0] - 1:
    # 2.1 时间不连续删除整个运动片段
    if d['时间'][i + 1] - d['时间'][i] > 3:
        # print("d['时间'][i + 1]="+str(d['时间'][i + 1])+"   d['时间'][i]="+str(d['时间'][i]))
        forward = i + 1  # 运动片段尾指针
        backward = i  # 运动片段头指针
        while d['GPS车速'][forward] >= 10 and forward < d.shape[0] - 1:
            # 非怠速
            forward += 1
        while (not (d['GPS车速'][backward - 1] >= 10 and d['GPS车速'][backward] <= 10)) and backward > 1:
            # 非怠速
            backward -= 1
        to_drop.append([backward, forward])
        i = forward + 1
        # print("#1   " + str(i))
        continue
    # 2.2 加速度异常删除整个运动片段
    if d['GPS车速'][i] > 100:
        len = i
        while d['GPS车速'][len] > 10 and len > 1:
            len -= 1
        if i - len < 7:
            forward = i + 1  # 运动片段尾指针
            backward = i  # 运动片段头指针
            while d['GPS车速'][forward] >= 10 and forward < d.shape[0] - 1:
                forward += 1
            while (not (d['GPS车速'][backward - 1] >= 10 and d['GPS车速'][backward] <= 10)) and backward > 1:
                backward -= 1
            to_drop.append([backward, forward])
            i = forward + 1
            # print("#2   " + str(i))
            continue
    # 2.3长期停车/怠速(停车超过180秒)
    if d['GPS车速'][i] < 10:
        forward = i
        while d['GPS车速'][forward] < 10 and forward < d.shape[0] - 1:
            forward += 1
        if (forward - i) > 180:
            # print("长期停车/怠速异常" + str(i))
            # 删剩180s
            to_drop.append([i, forward - 180])
            i = forward - 180 + 1
            # print("#3   " + str(i))
            continue
    i += 1
print("Intervals of dirty data:")
print(to_drop)

for x in to_drop:
    d = d.drop(d.index[x[0]:x[1]])
print("After data processing,data shape is:")
print(d.shape)

# write csv
print("Writing processed data...")
d.to_csv('processed_data/file1.csv', index=False)
print("Finish")

# line chart
