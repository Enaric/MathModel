# -*- coding: utf-8 -*-

import pandas as pd

# read csv
# d = pd.read_csv('processed_data/file1.csv')
d = pd.read_csv('processed_data/file2.csv')
# d = pd.read_csv('processed_data/file3.csv')
print(d.shape)

i = 0
spl = []
while i < d.shape[0] - 1:
    if d['GPS车速'][i] >= 10 and d['GPS车速'][i + 1] < 10:
        # end of a fragment
        spl.append(i)
    i += 1

print(spl)
label = 0
for k in range(len(spl)):
    new = d[label:spl[k] + 1]
    new = new.reset_index(drop=True)  # 重新进行index生成
    # new.to_csv('processed_data/file1_fragments/fragment' + str(k + 1) + '.csv', index=False)
    new.to_csv('processed_data/file2_fragments/fragment' + str(k + 1) + '.csv', index=False)
    # new.to_csv('processed_data/file3_fragments/fragment' + str(k + 1) + '.csv', index=False)
    label = spl[k] + 1
