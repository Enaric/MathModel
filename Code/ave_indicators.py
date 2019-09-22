# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


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


def cal_cluster():
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
    print("簇1----------------")
    cal(data, list0)
    print("簇2----------------")
    cal(data, list1)
    print("簇3----------------")
    cal(data, list2)
    print("簇4----------------")
    cal(data, list3)


def cal_total():
    loan_data = pd.read_csv("processed_data/fragments_set/all_file.csv")
    print(np.mean(loan_data))

def calculate(filePath):
    d = pd.read_csv(filePath)
    # print(d)

    # 运动时长
    total_time = d.shape[0]
    print("运动时长")
    print(total_time)

    # 平均速度
    ave_speed = format(np.mean(d['GPS车速']), '.2f')
    print("平均速度")
    print(ave_speed)

    # 平均行驶速度
    ave_runtime_speed = format(np.mean(d[d['GPS车速'] != 0]['GPS车速']), '.2f')
    print("平均行驶速度")
    print(ave_runtime_speed)

    acceleration_time = 0
    deceleration_time = 0
    acceleration_sum = 0
    deceleration_sum = 0
    for i in range(d.shape[0] - 1):
        if d['GPS车速'][i] < d['GPS车速'][i + 1]:
            acceleration_time += 1
            acceleration_sum += d['GPS车速'][i + 1] - d['GPS车速'][i]
        elif d['GPS车速'][i] > d['GPS车速'][i + 1]:
            deceleration_time += 1
            deceleration_sum += d['GPS车速'][i + 1] - d['GPS车速'][i]

    # 平均加速度
    if acceleration_time == 0:
        ave_acceleration = 0.00
    else:
        ave_acceleration = format(acceleration_sum / acceleration_time, '.2f')
    print("平均加速度")
    print(ave_acceleration)

    # 平均减速度
    if deceleration_time == 0:
        ave_deceleration = 0.00
    else:
        ave_deceleration = format(deceleration_sum / deceleration_time, '.2f')
    print("平均减速度")
    print(ave_deceleration)

    # 怠速时间比
    slow_rate = format(d[d['GPS车速'] == 0].shape[0] / d.shape[0], '.2f')
    print("怠速时间比")
    print(slow_rate)

    # 加速时间比
    acceleration_rate = format(acceleration_time / (d.shape[0] - 1), '.2f')
    print("加速时间比")
    print(acceleration_rate)

    # 减速时间比
    deceleration_rate = format(deceleration_time / (d.shape[0] - 1), '.2f')
    print("减速时间比")
    print(deceleration_rate)

    # 速度标准差
    std_speed = format(np.std(d['GPS车速'], ddof=1), '.2f')
    print("速度标准差")
    print(std_speed)

    acceleration = []
    for i in range(d.shape[0] - 1):
        acceleration.append(d['GPS车速'][i + 1] - d['GPS车速'][i])

    #加速度标准差
    std_acceleration = format(np.std(acceleration, ddof=1), '.2f')
    print("加速度标准差")
    print(std_acceleration)

def cal_final():
    calculate("clusterALL/final.csv")


if __name__ == '__main__':
    cal_cluster()  # 计算每个簇的各项指标平均值

    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("整体样本的各项指标平均值")
    cal_total()  # 计算整体样本的各项指标平均值

    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("最终曲线的各项指标平均值")
    cal_final()  # 计算最终曲线的各项指标平均值
