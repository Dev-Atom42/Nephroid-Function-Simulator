#!/usr/bin/python
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np

R = float(input(" a = "))
r = R/2
P = int(input("Size of primitive = "))



circumference = 360
x_points = []
y_points = []


print ("Nephroid")

for s in range(0,circumference):
    x = (R + r) * cos(radians(s)) - r * cos(radians(((R + r)/r)*s))
    y = (R + r) * sin(radians(s)) - r * sin(radians(((R + r)/r)*s))
    x_points.append(x)
    y_points.append(y)

raza = plt.Line2D((0, 0), (0, 0), linewidth=0, color="k", visible=False)
circler = plt.Circle((0, 0), r, color='r', fill=False, visible=False)
circleR = plt.Circle((0, 0), R, color='r', fill=False, visible=False)
punct = plt.Rectangle((0, 0), P/10, P/10, color="b", visible=True) 
#plt.Circle((0, 0), float(float(P)/10), color="b", visible=True)
fig, ax = plt.subplots()
ax.set_xlim(-2*(R + r),2*(R + r))
ax.set_ylim(-2*(R + r),2*(R + r))
trace, = ax.plot([], [], color="r")
ax.add_artist(circleR)
ax.add_artist(raza)
ax.add_artist(punct)
ax.add_artist(circler)
ax.add_artist(trace)

def init():
    circler.center = (x, y)
    punct.center = (x, y)
    ax.add_patch(circler)
    ax.add_patch(punct)
    return circler, punct,

def graphic(i):
    trace.set_data((x_points[:i], y_points[:i]))
    return trace,

def primitive(i):
    x = (r +  R) * np.cos(np.radians(i))
    y = (r + R) * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.set_width(P/10)
    punct.set_height(P/10)
    punct.set_xy([x2-(P/20), y2-(P/20)])
    return circler, punct, raza,

def full_animate(i):
    x = (r +  R) * np.cos(np.radians(i))
    y = (r + R) * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.set_width(P/10)
    punct.set_height(P/10)
    punct.set_xy([x2-(P/20), y2-(P/20)])
    trace.set_data((x_points[:i], y_points[:i]))    
    return circler, punct, raza, trace,

graphic(circumference)

anim = animation.FuncAnimation(fig, primitive,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)

plt.grid()
plt.show()
