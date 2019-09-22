# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 每个片段个数约为4，2，2，2

# processed_data/file2_fragments/fragment123.csv
# processed_data/file1_fragments/fragment747.csv
# processed_data/file1_fragments/fragment444.csv

# processed_data/file3_fragments/fragment4.csv
# processed_data/file3_fragments/fragment32.csv

# processed_data/file1_fragments/fragment923.csv
# processed_data/file2_fragments/fragment370.csv

# processed_data/file1_fragments/fragment118.csv
# processed_data/file1_fragments/fragment119.csv
# loan_data = pd.read_csv("processed_data/file2_fragments/fragment123.csv")
# X = loan_data["时间"] - min(loan_data["时间"])
# Y = loan_data
# plt.plot(X, Y)
# plt.show()

cluster1_1 = pd.read_csv("processed_data/file2_fragments/fragment123.csv")
cluster1_2 = pd.read_csv("processed_data/file1_fragments/fragment747.csv")
cluster1_3 = pd.read_csv("processed_data/file1_fragments/fragment444.csv")
cluster2_1 = pd.read_csv("processed_data/file3_fragments/fragment4.csv")
cluster2_2 = pd.read_csv("processed_data/file3_fragments/fragment32.csv")
cluster2_3 = pd.read_csv("processed_data/file2_fragments/fragment366.csv")
cluster3_1 = pd.read_csv("processed_data/file1_fragments/fragment923.csv")
cluster3_2 = pd.read_csv("processed_data/file2_fragments/fragment370.csv")
cluster4_1 = pd.read_csv("processed_data/file1_fragments/fragment118.csv")
cluster4_2 = pd.read_csv("processed_data/file1_fragments/fragment119.csv")
cluster4_3 = pd.read_csv("processed_data/file1_fragments/fragment412.csv")
cluster1 = pd.concat([cluster1_1, cluster1_2, cluster1_3], axis=0)
cluster2 = pd.concat([cluster2_1, cluster2_2, cluster2_3], axis=0)
cluster3 = pd.concat([cluster3_1, cluster3_2], axis=0)
cluster4 = pd.concat([cluster4_1, cluster4_2, cluster4_3], axis=0)
total = pd.concat([cluster4, cluster2, cluster1, cluster3], axis=0)
print(total)
total = total.reset_index()
plt.figure(figsize=(12.5, 4))
Y = total["GPS车速"]
plt.plot(Y)

plt.savefig('picture/k=4/fileALL/combined.jpg')
plt.show()
