# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

loan_data0 = pd.read_csv("clusterALL/cluster1/0.2730974019643578_-0.1256950062566616_-0.002283132279538051.csv",
                         usecols=["filePath"])
loan_data1 = pd.read_csv("clusterALL/cluster2/-0.07692966005390714_0.09021199409307053_0.03121459362565514.csv",
                         usecols=["filePath"])
loan_data2 = pd.read_csv("clusterALL/cluster3/0.566586257735794_0.07949322141100602_-0.020340358125649185.csv",
                         usecols=["filePath"])
loan_data3 = pd.read_csv("clusterALL/cluster4/-0.5658195986301829_-0.005295960143354379_-0.01051418281978004.csv",
                         usecols=["filePath"])

data = pd.read_csv("processed_data/fragments_set/all_file.csv")


list0 = []
list1 = []
list2 = []
list3 = []
for i in range(loan_data0.shape[0]):
    list0.append(loan_data0["filePath"][i])
for i in range(loan_data1.shape[0]):
    list1.append(loan_data1["filePath"][i])
for i in range(loan_data2.shape[0]):
    list2.append(loan_data2["filePath"][i])
for i in range(loan_data3.shape[0]):
    list3.append(loan_data3["filePath"][i])


def cal(data, list0):
    ave_speed = []
    ave_runtime_speed = []
    ave_acceleration = []
    ave_deceleration = []
    slow_rate = []
    acceleration_rate = []
    deceleration_rate = []
    std_speed = []
    std_acceleration = []
    for i in range(data.shape[0]):
        filePath = data["filePath"][i]
        if filePath in list0:
            ave_speed.append(data["平均速度"][i])
            ave_runtime_speed.append(data["平均行驶速度"][i])
            ave_acceleration.append(data["平均加速度"][i])
            ave_deceleration.append(data["平均减速度"][i])
            slow_rate.append(data["怠速时间比"][i])
            acceleration_rate.append(data["加速时间比"][i])
            deceleration_rate.append(data["减速时间比"][i])
            std_speed.append(data["速度标准差"][i])
            std_acceleration.append(data["加速度标准差"][i])
    print("平均速度")
    print(np.mean(ave_speed))
    print("平均行驶速度")
    print(np.mean(ave_runtime_speed))
    print("平均加速度")
    print(np.mean(ave_acceleration))
    print("平均减速度")
    print(np.mean(ave_deceleration))
    print("怠速时间比")
    print(np.mean(slow_rate))
    print("加速时间比")
    print(np.mean(acceleration_rate))
    print("减速时间比")
    print(np.mean(deceleration_rate))
    print("速度标准差")
    print(np.mean(std_speed))
    print("加速度标准差")
    print(np.mean(std_acceleration))

print("簇1----------------")
cal(data, list0)
print("簇2----------------")
cal(data, list1)
print("簇3----------------")
cal(data, list2)
print("簇4----------------")
cal(data, list3)
