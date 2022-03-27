#!/usr/bin/python
#copyright(c) strongnine
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from pyts.image import GramianAngularField

sin_data = np.loadtxt('./data/sinx.csv', delimiter=",", skiprows=0).reshape(1, -1)  # 加载数据 (load the source data)
image_size = 28  # 生成的 GAF 图片的大小 (the size of each GAF image)

# `method` 的可选参数有：`summation` and `difference`
# The optional parameters of argument `method`: `summation` and `difference`
gasf = GramianAngularField(image_size=image_size, method='summation')
sin_gasf = gasf.fit_transform(sin_data)

gadf = GramianAngularField(image_size=image_size, method='difference')
sin_gadf = gadf.fit_transform(sin_data)
imges = [sin_gasf[0], sin_gadf[0]]
titles = ['Summation', 'Difference']

# 两种方法的可视化差异对比
# Comparison of two different methods
fig, axs = plt.subplots(1, 2, constrained_layout=True)
for img, title, ax in zip(imges, titles, axs):
    ax.imshow(img)
    ax.set_title(title)
fig.suptitle('GramianAngularField', y=0.94, fontsize=16)
plt.margins(0, 0)
plt.savefig("./GramianAngularField.pdf", pad_inches=0)
plt.show()

image.imsave("./images/GAF_of_Sin.png", sin_gasf[0])  # 保存图片 (save image)