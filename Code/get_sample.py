# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath0 = 'cluster/cluster1/-0.6421359708185889_0.014605582678106698_-0.03844262436214339.csv'
filePath1 = 'cluster/cluster2/0.4598567108240415_0.10776014715803317_-0.060686486011832484.csv'
filePath2 = 'cluster/cluster3/-0.1299293005749705_0.09195986100270996_0.05644192446732742.csv'
filePath3 = 'cluster/cluster4/0.2051833116979913_-0.19156251659036425_0.03593441679764642.csv'

cluster_center0 = [-0.6421359708185889, 0.014605582678106698, -0.03844262436214339]
cluster_center1 = [0.4598567108240415, 0.10776014715803317, -0.060686486011832484]
cluster_center2 = [-0.1299293005749705, 0.09195986100270996, 0.05644192446732742]
cluster_center3 = [0.2051833116979913, -0.19156251659036425, -0.03593441679764642]


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


print(simple0)  # processed_data/file1_fragments/fragment594.csv
print(simple1)  # processed_data/file1_fragments/fragment1167.csv
print(simple2)  # processed_data/file1_fragments/fragment793.csv
print(simple3)  # processed_data/file1_fragments/fragment101.csv


def draw_simple(filePath, cluster):
    loan_data = pd.read_csv(filePath)
    X = loan_data["时间"]-min(loan_data["时间"])
    Y = loan_data["GPS车速"]
    plt.plot(X, Y)
    plt.plot(max(X+1),0)
    plt.savefig('picture/k=4/cluster' + str(cluster) + '.jpg')
    plt.show()
    # print(loan_data)


draw_simple("processed_data/file1_fragments/fragment594.csv", 0)
draw_simple("processed_data/file1_fragments/fragment1167.csv", 1)
draw_simple("processed_data/file1_fragments/fragment793.csv", 2)
draw_simple("processed_data/file1_fragments/fragment101.csv", 3)
