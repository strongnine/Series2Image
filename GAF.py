import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GASF, GADF

x = np.loadtxt(open("sinx.csv","rb"),delimiter=",",skiprows=0).T
# print(type(x),x.shape)

X = x[0:]
X = X.reshape(1, -1)
print(type(X),X.shape)
image_size = 28
gasf = GASF(image_size)
X_gasf = gasf.fit_transform(X)
print(X_gasf.shape)
print(X_gasf[0,4,2],X_gasf[0,2,4])
gadf = GADF(image_size)
X_gadf = gadf.fit_transform(X)
print(X_gadf[0,1,2],X_gadf[0,2,1])

# Show the results for the first time series
plt.figure(figsize=(16, 8))
plt.subplot(121)
plt.imshow(X_gasf[0], cmap='rainbow', origin='lower')
plt.title("GASF", fontsize=16)
plt.subplot(122)
plt.imshow(X_gadf[0], cmap='rainbow', origin='lower')
plt.title("GADF", fontsize=16)
plt.savefig('sinx.jpg')
plt.show()

