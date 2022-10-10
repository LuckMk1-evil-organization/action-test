# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

flag = np.zeros((500,1000,3), dtype = np.uint8)

x1 = np.linspace(-375.5, 624.5, 1000)
y1 = np.linspace(-249.5, 249.5, 500)
x2 = np.linspace(-624.5, 375.5, 1000)
y2 = np.linspace(-249.5, 249.5, 500)

X1, Y1 = np.meshgrid(x1,y1, indexing='xy')
X2, Y2 = np.meshgrid(x2,y2, indexing='xy')

r = 200

flag[:,:] = 28, 105, 158

vert = ((X1*X1 + Y1*Y1 <= r*r) & (X1*X1 + Y1*Y1 >= (r*r/1.4)))

orange = (X2*X2 + Y2*Y2 <= r*r) & (X2*X2 + Y2*Y2 >= (r*r/1.4))

#vert2 = 

flag[vert, :] = [39,141,39]
flag[orange, :] = [216, 101, 0]

vert2 = ((X1*X1 + Y1*Y1 <= r*r) & (X1*X1 + Y1*Y1 >= (r*r/1.4))) & (Y1<0)

flag[vert2, :] = [39,141,39]

plt.imshow(flag)
plt.imsave("anneaux.png", flag)
