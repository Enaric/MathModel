# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath0 = 'clusterALL/cluster1/0.2730974019643578_-0.1256950062566616_-0.002283132279538051.csv'
filePath1 = 'clusterALL/cluster2/-0.07692966005390714_0.09021199409307053_0.03121459362565514.csv'
filePath2 = 'clusterALL/cluster3/0.566586257735794_0.07949322141100602_-0.020340358125649185.csv'
filePath3 = 'clusterALL/cluster4/-0.5658195986301829_-0.005295960143354379_-0.01051418281978004.csv'

cluster_center0 = [0.2730974019643578, -0.1256950062566616, -0.002283132279538051]
cluster_center1 = [-0.07692966005390714, 0.09021199409307053, 0.03121459362565514]
cluster_center2 = [0.566586257735794, 0.07949322141100602, -0.020340358125649185]
cluster_center3 = [-0.5658195986301829, -0.005295960143354379, -0.01051418281978004]


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


print(simple0)
# processed_data/file2_fragments/fragment123.csv
# processed_data/file1_fragments/fragment747.csv
# processed_data/file1_fragments/fragment444.csv
print(simple1)
# processed_data/file3_fragments/fragment4.csv
# processed_data/file3_fragments/fragment32.csv
# processed_data/file2_fragments/fragment366.csv
print(simple2)
# processed_data/file1_fragments/fragment923.csv
# processed_data/file2_fragments/fragment370.csv
print(simple3)
# processed_data/file1_fragments/fragment118.csv
# processed_data/file1_fragments/fragment119.csv
# processed_data/file1_fragments/fragment412.csv


def draw_simple(filePath, cluster):
    loan_data = pd.read_csv(filePath)
    X = loan_data["时间"]-min(loan_data["时间"])
    Y = loan_data["GPS车速"]
    plt.plot(X, Y)
    plt.plot(max(X+1),0)
    plt.savefig('picture/k=4/fileALL/cluster' + str(cluster) + '.jpg')
    plt.show()
    # print(loan_data)


draw_simple("processed_data/file2_fragments/fragment123.csv", 0)
draw_simple("processed_data/file3_fragments/fragment4.csv", 1)
draw_simple("processed_data/file1_fragments/fragment923.csv", 2)
draw_simple("processed_data/file1_fragments/fragment119.csv", 3)
