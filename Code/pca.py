# -*- coding: utf-8 -*-
# 主成分分析 降维
import pandas as pd

# TODO 待完善


# 参数初始化
inputfile = 'processed_data/fragments_set/file1.csv'
outputfile = 'processed_data/fragments_set/file1_pca.csv'  # 降维后的数据

data = pd.read_csv(inputfile)  # 读入数据

# 检测 nan
# print(data)
# print(data.isnull().any())
# predict_null = pd.isnull(data['加速度标准差'])
# data_null = data[predict_null == True]
# print(data_null)

from sklearn.decomposition import PCA

pca = PCA()  # 保留所有成分
pca.fit(data)
print(pca.components_)  # 返回模型的各个特征向量
print(pca.explained_variance_ratio_)  # 返回各个成分各自的方差百分比(也称贡献率）

pca = PCA(1)  # 选取累计贡献率大于80%的主成分（1个主成分）
pca.fit(data)
low_d = pca.transform(data)  # 降低维度
pd.DataFrame(low_d).to_csv(outputfile)  # 保存结果
