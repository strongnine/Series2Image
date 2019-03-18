#!/usr/bin/python
#copyright(c) strongnine
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GASF, GADF
import time

csv_path = 'path_to_your_csv_file'
x = np.loadtxt(open("filename.csv","rb"),delimiter=",",skiprows=0).T

im_size = 256
im_sum = 5000
save_path = 'path_to_sava_jpg/'

for i in range(im_sum):
    ind = str(i).zfill(8)
    X = x[0,100*i:100*i+im_size]
    X = X.reshape(1, -1)
    
    gasf = GASF(im_size)
    X_gasf = gasf.fit_transform(X)
    # print(X_gasf.shape) # (1, 256, 256)
    X_gasf[0] = np.dot(X_gasf[0],100)
    gaf = X_gasf[0].astype('int')
    # print(gaf.dtype)

    # Show the results for the first time series
    plt.figure(figsize=(8, 8))
    plt.imshow(gaf, cmap='rainbow', origin='lower')
    # plt.title("GASF", fontsize=16)
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('.jpg',bbox_inches='tight',pad_inches = 0)
    # plt.show()
    plt.close('all')

    # show the processed/rest per 250 images
    if not(i%250):
        print(str(i)+'/'+str(im_sum))
    
    del(X_gasf, gaf, X, gasf, ind)

print('done')
