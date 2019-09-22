# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import csv


def calculate(filePath):
    d = pd.read_csv(filePath)
    # print(d)

    # 运动时长
    total_time = d.shape[0]

    # 平均速度
    ave_speed = format(np.mean(d['GPS车速']), '.2f')
    # print("平均速度")
    # print(ave_speed)

    # 平均行驶速度
    ave_runtime_speed = format(np.mean(d[d['GPS车速'] >= 10]['GPS车速']), '.2f')
    # print("平均行驶速度")
    # print(ave_runtime_speed)

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
    # print("平均加速度")
    # print(ave_acceleration)

    # 平均减速度
    if deceleration_time == 0:
        ave_deceleration = 0.00
    else:
        ave_deceleration = format(deceleration_sum / deceleration_time, '.2f')
    # print("平均减速度")
    # print(ave_deceleration)

    # 怠速时间比
    slow_rate = format(d[d['GPS车速'] < 10].shape[0] / d.shape[0], '.2f')
    # print("怠速时间比")
    # print(slow_rate)

    # 加速时间比
    acceleration_rate = format(acceleration_time / (d.shape[0] - 1), '.2f')
    # print("加速时间比")
    # print(acceleration_rate)

    # 减速时间比
    deceleration_rate = format(deceleration_time / (d.shape[0] - 1), '.2f')
    # print("减速时间比")
    # print(deceleration_rate)

    # 速度标准差
    std_speed = format(np.std(d['GPS车速'], ddof=1), '.2f')
    # print("速度标准差")
    # print(std_speed)

    acceleration = []
    for i in range(d.shape[0] - 1):
        acceleration.append(d['GPS车速'][i + 1] - d['GPS车速'][i])
    # 加速度标准差
    # print(acceleration)
    std_acceleration = format(np.std(acceleration, ddof=1), '.2f')
    # print("加速度标准差")
    # print(std_acceleration)

    line = [filePath, ave_speed, ave_runtime_speed, ave_acceleration, ave_deceleration, slow_rate,
            acceleration_rate, deceleration_rate, std_speed, std_acceleration]

    # out = open('processed_data/fragments_set/file1.csv', 'a', newline='')
    # out = open('processed_data/fragments_set/file2.csv', 'a', newline='')
    # out = open('processed_data/fragments_set/file3.csv', 'a', newline='')
    out = open('processed_data/fragments_set/all_file.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(line)


if __name__ == '__main__':
    for i in range(1181):
        calculate("processed_data/file1_fragments/fragment" + str(i + 1) + ".csv")
    for i in range(725):
        calculate("processed_data/file2_fragments/fragment" + str(i + 1) + ".csv")
    for i in range(649):
        calculate("processed_data/file3_fragments/fragment" + str(i + 1) + ".csv")
