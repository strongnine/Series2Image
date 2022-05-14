#!/usr/bin/python
#copyright(c) strongnine
# 批量生成 GAF 图片的代码 (Generate GAF images in batches)
# 将文件夹中的每个文件都生成一个 GAF 图 (...)
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from pyts.image import GramianAngularField

# 根据自己的需求修改一下变量的参数
dirname = "./data/dataset"  # 要处理的文件夹路径
savepath = "./data"         # GAF 图片保存的路径
img_sz = 28           # 确定生成的 GAF 图片的大小
method = 'summation'  # GAF 图片的类型，可选 'summation'（默认）和 'difference'


# 以下是 GAF 生成的代码
print("GAF 生成方法：%s，图片大小：%d * %d" % (method, img_sz, img_sz))
img_path = "%s/images" % savepath     # 可视化图片保存的文件夹
data_path = "%s/data_mat" % savepath  # 数据文件保存的文件夹
if not os.path.exists(img_path):
    os.makedirs(img_path)  # 如果文件夹不存在就创建一个
if not os.path.exists(data_path):
    os.makedirs(data_path)  # 如果文件夹不存在就创建一个

print("开始生成...")
print("可视化图片保存在文件夹 %s 中，数据文件保存在文件夹 %s 中。" % (img_path, data_path))
gaf = GramianAngularField(image_size=img_sz, method=method)
img_num = 0  # 计算生成的图片个数
for fname in os.listdir(dirname):
    filename, ext = os.path.splitext(fname)
    if ext != '.csv': continue  # 如果不是 csv 文件则跳过
    img_num += 1

    src_data = np.loadtxt("{}/{}".format(dirname, fname), delimiter=",")  # 加载数据 (load the source data)
    x = src_data.reshape(1, -1)
    img_gaf = gaf.fit_transform(x)

    img_save_path = "%s/%s.png" % (img_path, filename)
    image.imsave(img_save_path, img_gaf[0])  # 保存图片 (save image)

    data_save_path = "%s/%s.csv" % (data_path, filename)
    np.savetxt(data_save_path, img_gaf[0], delimiter=',')  # 保存数据为 csv 文件

print("生成完成，共处理 %d 个图片。" % img_num)