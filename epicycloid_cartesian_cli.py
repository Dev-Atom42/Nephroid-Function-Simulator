#!/usr/bin/python3
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np

R = float(input("R = "))
r = float(input("r = "))
P = int(input("Size of primitive = "))

if R >= r:
    circumference = 360
else:
    circumference = ceil(360 * (r/R))

x_points = []
y_points = []

print("Epicycloid cartesian")

for s in range(0,circumference):
    x = (R + r) * cos(radians(s)) - r * cos(radians(((R + r)/r)*s))
    y = (R + r) * sin(radians(s)) - r * sin(radians(((R + r)/r)*s))
    x_points.append(x)
    y_points.append(y)

raza = plt.Line2D((0, 0), (0, 0), linewidth=0, color="k", visible=False)
circler = plt.Circle((0, 0), r, color='r', fill=False, visible=False)
circleR = plt.Circle((0, 0), R, color='r', fill=False, visible=False)
punct = plt.Rectangle((0, 0), P, P, color="b", visible=True) 
plt.Circle((0, 0), float(float(P)), color="b", visible=True)
fig, ax = plt.subplots()
ax.set_xlim(-1.5*(R + r),1.5*(R + r))
ax.set_ylim(-1.5*(R + r),1.5*(R + r))
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
    punct.set_width(P)
    punct.set_height(P)
    punct.set_xy([x2-(P/2), y2-(P/2)])
    return circler, punct, raza,

def full_animate(i):
    x = (r +  R) * np.cos(np.radians(i))
    y = (r + R) * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.set_width(P)
    punct.set_height(P)
    punct.set_xy([x2-(P)/2, y2-(P)/2])
    trace.set_data((x_points[:i], y_points[:i]))    
    return circler, punct, raza, trace,

graphic(circumference)

anim = animation.FuncAnimation(fig, primitive,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)


plt.axis('scaled')

if (R-r) != 0:
    if R > r:
        plt.axis([-6*(R-r), 6*(R-r), -6*(R-r), 6*(R-r)])
    elif R < r:
        plt.axis([-6*(r-R), 6*(r-R), -6*(r-R), 6*(r-R)])
else:
    plt.axis([-3.5*R, 3.5*R, -3.5*R, 3.5*R])

plt.grid()
plt.show()
