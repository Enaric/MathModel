from scipy.stats import chi2_contingency
import numpy as np

kf_data = np.array([[19.05, 26.83, 1.59, 1.99, 0.29, 0.38, 0.30, 17.80, 2.34],
                    [16.21, 28.10, 2.75, 3.01, 0.39, 0.32, 0.28, 11.04, 2.93]])
kf = chi2_contingency(kf_data)
print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s' % kf)
