# -*- coding: utf-8 -*-

# 主成分分析 降维
import pandas as pd

inputfile = 'processed_data/fragments_set/file1.csv'
outputfile = 'processed_data/fragments_set/file1_pca.csv'  # 降维后的数据

data = pd.read_csv(inputfile)  # 读入数据


# 数据标准化
# 1、min-max标准化（Min-Max Normalization）
def min_max(data):
    return (data - data.min()) / (data.max() - data.min())


# 2、Z-score标准化方法(主成分太多了，没有用这种方法)
def Z_score(data):
    return (data - data.mean()) / (data.std())


data_norm = min_max(data)
print(data_norm)
# 检测 nan
# print(data)
# print(data.isnull().any())
# predict_null = pd.isnull(data['加速度标准差'])
# data_null = data[predict_null == True]
# print(data_null)

from sklearn.decomposition import PCA

pca = PCA()  # 保留所有成分
pca.fit(data_norm)
print(pca.components_)  # 返回模型的各个特征向量
print('每个成分各自方差百分比 :')
print(pca.explained_variance_ratio_)  # 返回各个成分各自的方差百分比(也称贡献率）

pca = PCA(3)  # 选取累计贡献率大于80%的主成分（1个主成分）
pca.fit(data_norm)
low_d = pca.transform(data_norm)  # 降低维度
pd.DataFrame(low_d).to_csv(outputfile)  # 保存结果
