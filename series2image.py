#!/usr/bin/python
#copyright(c) strongnine
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from pyts.image import GramianAngularField
import time

data = np.loadtxt('data.csv', delimiter=",").reshape(1, -1)
_, n_sample = data.shape

im_size = 128
step = 16  # step of slide window
im_sum = (n_sample - im_size) // step
save_path = './images/'

gasf = GramianAngularField(image_size=im_size, method='summation')
for i in range(17):
    start_index, end_index = i * step, i * step + im_size
    sub_series = data[:, start_index:end_index]
    GAF_gasf = gasf.fit_transform(sub_series)
    im = GAF_gasf[0]
    filename = save_path + '%d.png' % i
    image.imsave(filename, im)
