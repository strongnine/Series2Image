# Series2Image

使用 Python 的 [pyts](https://pyts.readthedocs.io/en/stable/) 库将一维时间序列编码为二维图片，这样可以用于训练卷积神经网络（CNN）

更多详细的内容参考 CSDN 博客：

1. [将一维时间序列转化成二维图片](https://blog.csdn.net/weixin_39679367/article/details/86416439)
2. [Python：使用 pyts 把一维时间序列转换成二维图片](https://blog.csdn.net/weixin_39679367/article/details/88653018)

2022 年 03 月 27 号更新：

1. `src/paa.py`：PAA 算法的代码；
2. `src/GAF.py`：GAF 基础 demo；
3. `src/slide_window.py`：利用 滑动窗口 将一个长的序列信号生成多个 GAF 图片；
4. `src/batch_gen.py`：数据矩阵中的每一列生成对应的 GAF 图；



---



Encoding time series as images using GAF operation by `pyts`. 

see more in CSDN Blogs: 

1. [将一维时间序列转化成二维图片](https://blog.csdn.net/weixin_39679367/article/details/86416439)
2. [Python：使用 pyts 把一维时间序列转换成二维图片](https://blog.csdn.net/weixin_39679367/article/details/88653018)

2022.03.27 update:

1. `src/paa.py`：PAA algorithm code；
2. `src/GAF.py`：GAF demo；
3. `src/slide_window.py`：Using a sliding window to generate GAF images from a long sequence of signals; 
4. `src/batch_gen.py`：Generate GAF images in batches, each column in the data file generate a GAF image;



