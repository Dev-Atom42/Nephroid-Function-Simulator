#!/usr/bin/python3
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np
  
a = float(input("a = "))
b = float(input("b = "))
P = int(input("Size of primitive = "))

if a >= b:
    theta = np.pi * 2
else:
    theta = np.pi * 2 * (b/a)

rads = np.arange(0, (theta), 0.01)
circumference = len(rads)
r_points = []

print("Epicycloid polar")

for rad in rads:
    r = np.sqrt(pow(a + b, 2) + pow(b, 2) - 2 * b * (a + b) * np.cos((a/b) * rad))
    r_points.append(r)

punct = plt.Rectangle((0, 0), P, P, color="b", visible=True)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
trace, = ax.plot([], [], color="r")
ax.grid(True)
ax.add_artist(punct)
ax.add_artist(trace)

if (a-b) != 0:
    if a > b:
        ax.set_rmax(6*(a-b))
    elif a < b:
        ax.set_rmax(6*(b-a))
else:
    ax.set_rmax(3.5*a)

def init():
    ax.add_patch(punct)
    return punct,

def graphic(i):
    trace.set_data((rads[:i], r_points[:i]))
    return trace,

def primitive(i):
    x2 = rads[i]
    y2 = r_points[i]
    punct.set_width(P/(4*a))
    punct.set_height(P)
    punct.set_xy([x2-(P/(8*a)), y2-(P/2)])
    return punct,

graphic(circumference)
anim = animation.FuncAnimation(fig, primitive,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)
plt.show()
