#!/usr/bin/python
#copyright(c) strongnine
# 批量生成 GAF 图片的代码 (Generate GAF images in batches)
# 数据矩阵中的每一列生成对应的 GAF 图 (Each column in the data file generate a GAF image)
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from pyts.image import GramianAngularField

# 根据自己的需求修改一下变量的参数
filename = "./data/data_mat.csv"  # 要处理的文件路径
savepath = "./data"               # GAF 图片保存的路径
img_sz = 28           # 确定生成的 GAF 图片的大小
method = 'summation'  # GAF 图片的类型，可选 'summation'（默认）和 'difference'

# 以下是 GAF 生成的代码
print("GAF 生成方法：%s，图片大小：%d * %d" % (method, img_sz, img_sz))
img_path = "%s/images" % savepath  # 可视化图片保存的文件夹
data_path = "%s/data" % savepath   # 数据文件保存的文件夹
if not os.path.exists(img_path):
    os.makedirs(img_path)   # 如果文件夹不存在就创建一个
if not os.path.exists(data_path):
    os.makedirs(data_path)  # 如果文件夹不存在就创建一个

print("开始生成...")
print("可视化图片保存在文件夹 %s 中，数据文件保存在文件夹 %s 中。" % (img_path, data_path))
src_data = np.loadtxt(filename, delimiter=",")  # 加载数据 (load the source data)
img_num = src_data.shape[1]  # 生成图片的总数为数据矩阵的列数 (the total numbers of GAF images)
gaf = GramianAngularField(image_size=img_sz, method=method)
gaf_images = gaf.fit_transform(src_data.T)

# gaf_images 的 shape 为 （img_num, img_sz, img_sz)
for i in range(img_num):  # 把每个图片都保存起来
    gaf_img = gaf_images[i, :, :]  # 得到第 i 个图片的数据
    img_save_path = "%s/%d.png" % (img_path, i)
    data_save_path = "%s/%d.csv" % (data_path, i)
    image.imsave(img_save_path, gaf_img)                # 保存图片 (save image)
    np.savetxt(data_save_path, gaf_img, delimiter=',')  # 保存数据为 csv 文件

print("生成完成，共处理 %d 个图片。" % img_num)