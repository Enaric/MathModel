# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath0 = 'cluster/cluster1/-0.5173846438817027_0.05613012595157204_-0.002536207511098446.csv'
filePath1 = 'cluster/cluster2/0.4214707755895102_0.10000164458837456_-0.01591727130848888.csv'
filePath2 = 'cluster/cluster3/0.07423795298071396_-0.22908419444423603_0.01115025977150878.csv'
filePath3 = 'cluster/cluster4/-0.04781599251265637_0.1815417183243165_0.007219086865307944.csv'

cluster_center0 = [-0.5173846438817027, 0.05613012595157204, -0.002536207511098446]
cluster_center1 = [0.4214707755895102, 0.10000164458837456, -0.01591727130848888]
cluster_center2 = [0.07423795298071396, -0.22908419444423603, 0.01115025977150878]
cluster_center3 = [-0.04781599251265637, 0.1815417183243165, 0.007219086865307944]


# 计算最接近簇心的科学运动片段
# 欧几里得距离
def get_sample(filePath, cluster_center):
    loan_data = pd.read_csv(filePath)

    loan_data['distant'] = ((loan_data['0'] - cluster_center[0]) ** 2 + (
            loan_data['1'] - cluster_center[1]) ** 2 + (
                                    loan_data['2'] - cluster_center[2]) ** 2) ** 0.5
    return loan_data[loan_data['distant'] == loan_data['distant'].min()]


simple0 = get_sample(filePath0, cluster_center0)
simple1 = get_sample(filePath1, cluster_center1)
simple2 = get_sample(filePath2, cluster_center2)
simple3 = get_sample(filePath3, cluster_center3)


# print(simple0)  # processed_data/file1_fragments/fragment932.csv
# print(simple1)  # processed_data/file1_fragments/fragment189.csv
# print(simple2)  # processed_data/file1_fragments/fragment855.csv
# print(simple3)  # processed_data/file1_fragments/fragment1304.csv


def draw_simple(filePath, cluster):
    loan_data = pd.read_csv(filePath)
    X = loan_data["时间"]-min(loan_data["时间"])
    Y = loan_data["GPS车速"]
    plt.plot(X, Y)
    plt.savefig('picture/k=4/cluster' + str(cluster) + '.jpg')
    plt.show()
    # print(loan_data)


draw_simple("processed_data/file1_fragments/fragment932.csv", 0)
draw_simple("processed_data/file1_fragments/fragment189.csv", 1)
draw_simple("processed_data/file1_fragments/fragment855.csv", 2)
draw_simple("processed_data/file1_fragments/fragment1304.csv", 3)
