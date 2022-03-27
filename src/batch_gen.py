#!/usr/bin/python
#copyright(c) strongnine
# 批量生成 GAF 图片的代码 (Generate GAF images in batches)
# 数据矩阵中的每一列生成对应的 GAF 图 (Each column in the data file generate a GAF image)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from pyts.image import GramianAngularField

src_data = np.loadtxt("./data/data_mat.csv", delimiter=",")  # 加载数据 (load the source data)
img_num = src_data.shape[1]  # 生成图片的总数为数据矩阵的列数 (the total numbers of GAF images)
img_sz = 28  # 生成的 GAF 图片的大小 (the size of each GAF image)

# `method` 的可选参数有：`summation` and `difference`
# The optional parameters of argument `method`: `summation` and `difference`
gaf = GramianAngularField(image_size=img_sz, method='summation')

for i in range(img_num):
    x = src_data[:, i].reshape(1, -1)  # 得到单独一列的数据 (get a single column of data)
    img_gaf = gaf.fit_transform(x)  # 由序列信号转化为 GAF 图 (Convert from sequence signal to GAF image)
    image.imsave("./images/%d.png" % i, img_gaf[0])  # 保存图片 (save image)
    