#!/usr/bin/python
#copyright(c) strongnine
import numpy as np
import matplotlib.pyplot as plt
from pyts.approximation import PiecewiseAggregateApproximation

data = np.loadtxt("./data/data.csv", delimiter=',')
data = data.reshape(1, -1)
n_sampels, n_timestamps = data.shape
n_paa = 128
window_size = n_timestamps // n_paa
paa = PiecewiseAggregateApproximation(window_size=window_size)
X_paa = paa.transform(data)[:, :n_paa]
# np.savetxt("./paa_result.csv", X_paa.T, fmt='%.18f')

plt.figure(figsize=(6, 4))
plt.plot(data[0], 'o--', ms=0.1, label='Original', linewidth=1.)
plt.plot(np.arange(window_size // 2,
                   n_timestamps + window_size // 2,
                   window_size)[:n_paa], X_paa[0], 'o--', ms=2.5, label='PAA', linewidth=1.)
plt.show()