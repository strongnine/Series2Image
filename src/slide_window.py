#!/usr/bin/python
#copyright(c) strongnine
# 利用 滑动窗口 将一个长的序列信号生成多个 GAF 图片
# Using a sliding window to generate GAF images from a long sequence of signals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from pyts.image import GramianAngularField

data = np.loadtxt('./data/data.csv', delimiter=",").reshape(1, -1)
_, n_sample = data.shape

im_size = 128  # 生成的 GAF 图片的大小 (the size of each GAF image)
step = 16  # 滑动窗口的步长 (step of slide window)
im_sum = (n_sample - im_size) // step  # 生成图片的总数 (the total numbers of GAF images)
save_path = './images/'  # 图片保存的路径 (save path of the GAF images)

gasf = GramianAngularField(image_size=im_size, method='summation')
for i in range(17):
    start_index, end_index = i * step, i * step + im_size
    sub_series = data[:, start_index:end_index]
    GAF_gasf = gasf.fit_transform(sub_series)
    im = GAF_gasf[0]
    filename = save_path + '%d.png' % i
    image.imsave(filename, im)
