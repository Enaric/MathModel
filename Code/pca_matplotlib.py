# -*- coding: utf-8 -*-

# 主成分分析 降维
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Y = [1760,1280,780,500,450,400,360,340]
Z = [1,2,3,4,5,6,7,8]


plt.plot(Z,Y)
plt.savefig('picture/pca.jpg')
plt.show()