from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

loan_data = pd.read_csv('processed_data/fragments_set/file1_pca.csv')
# print(loan_data.head())

# 设置要进行聚类的字段
loan = np.array(loan_data[['PC1', 'PC2', 'PC3']])
# 设置类别为3
clf = KMeans(n_clusters=4)
# 将数据代入到聚类模型中
clf = clf.fit(loan)

print(clf.cluster_centers_)
loan_data['label'] = clf.labels_
print(loan_data.head())

# 提取不同类别的数据
loan_data0 = loan_data.loc[loan_data["label"] == 0]
loan_data1 = loan_data.loc[loan_data["label"] == 1]
loan_data2 = loan_data.loc[loan_data["label"] == 2]
loan_data3 = loan_data.loc[loan_data["label"] == 3]

loan_data0.to_csv("cluster/cluster1/set.csv")
loan_data1.to_csv("cluster/cluster2/set.csv")
loan_data2.to_csv("cluster/cluster3/set.csv")
loan_data3.to_csv("cluster/cluster4/set.csv")
# TODO 聚类结果作图
