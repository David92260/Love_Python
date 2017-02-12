#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Python code for Saint Valentin !!!
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,2))

ax1 = fig.add_subplot(1,4,1)
plt.axis([0, 0.6, 0.1, 100])
x_1 = np.arange(0.01,0.5,0.001)
y_1 = 1/x_1
ax1.xaxis.set_major_formatter(plt.NullFormatter())
ax1.yaxis.set_major_formatter(plt.NullFormatter())
ax1.plot(x_1, y_1, 'r-',linewidth=4)

ax2 = fig.add_subplot(1,4,2)
plt.axis('equal')
an = np.linspace(0, 2*np.pi, 100)
ax2.xaxis.set_major_formatter(plt.NullFormatter())
ax2.yaxis.set_major_formatter(plt.NullFormatter())
ax2.plot(3*np.cos(an), 3*np.sin(an), 'r-',linewidth=4)

ax3 = fig.add_subplot(1,4,3)
x_3 = np.arange(-3,3,0.01)
y_3 = abs(-2*x_3)
ax3.xaxis.set_major_formatter(plt.NullFormatter())
ax3.yaxis.set_major_formatter(plt.NullFormatter())
ax3.plot(x_3, y_3, 'r-',linewidth=4)

ax4 = fig.add_subplot(1,4,4)
plt.axis([-4, 1, -np.pi,np.pi])
y_4 = np.arange(-np.pi,np.pi,0.01)
x_4 = -3*abs(np.sin(y_4))
ax4.xaxis.set_major_formatter(plt.NullFormatter())
ax4.yaxis.set_major_formatter(plt.NullFormatter())
ax4.plot(x_4, y_4, 'r-',linewidth=4)

plt.show()
