import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField

sin_data = np.loadtxt('sinx.csv', delimiter=",", skiprows=0).reshape(1, -1)
image_size = 28

gasf = GramianAngularField(image_size=image_size, method='summation')
sin_gasf = gasf.fit_transform(sin_data)
gadf = GramianAngularField(image_size=image_size, method='difference')
sin_gadf = gadf.fit_transform(sin_data)
images = [sin_gasf[0], sin_gadf[0]]
titles = ['Summation', 'Difference']

fig, axs = plt.subplots(1, 2, constrained_layout=True)
for image, title, ax in zip(images, titles, axs):
    ax.imshow(image)
    ax.set_title(title)
fig.suptitle('GramianAngularField', y=0.94, fontsize=16)
plt.margins(0, 0)
plt.savefig("GramianAngularField.pdf", pad_inches=0)
plt.show()
