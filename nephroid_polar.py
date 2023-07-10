#!/usr/bin/python3
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np
  
a = float(input(" a = "))/2
P = int(input("Size of primitive = "))

theta = np.pi * 2
rads = np.arange(0, (theta), 0.01)
circumference = len(rads)
r_points = []

print("Nephroid polar")

for rad in rads:
    r = np.sqrt(2) * a * pow(( pow(1-np.cos(rad), 1/3) + pow(np.cos(rad) + 1, 1/3) ), 3/2)
    r_points.append(r)

punct = plt.Rectangle((0, 0), 1/16, 1, color="b", visible=True)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
trace, = ax.plot([], [], color="r")
ax.grid(True)
ax.add_artist(punct)
ax.add_artist(trace)

ax.set_rmax(4.4*a)

def init():
    ax.add_patch(punct)
    return punct,

def graphic(i):
    trace.set_data((rads[:i], r_points[:i]))
    return trace,

def primitive(i):
    x2 = rads[i]
    y2 = r_points[i]
    punct.set_width(P/10)
    punct.set_height(P/10)
    punct.set_xy([x2-(P/20), y2-(P/20)])
    return punct,

graphic(circumference)
anim = animation.FuncAnimation(fig, primitive,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)
plt.show()

