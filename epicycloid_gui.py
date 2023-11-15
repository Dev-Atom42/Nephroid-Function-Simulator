#!/usr/bin/python3
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import numpy as np

def cartesian():
	global canvas
	if canvas:
	    canvas.get_tk_widget().destroy()	

	plt.close('all')

	R = RSize.get() #Радиус большей окружности.
	r = rSize.get() #Радиус малой окружности.
	P = primitiveSize.get()

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
	punct = plt.Rectangle((0, 0), P, P, color="b", visible=Var1.get()) 
	plt.Circle((0, 0), float(float(P)), color="b", visible=True)
	fig, ax = plt.subplots()
	ax.clear()
	ax.set_xlim(-1.5*(R + r),1.5*(R + r))
	ax.set_ylim(-1.5*(R + r),1.5*(R + r))
	trace, = ax.plot([], [], color="r")

	ax.add_artist(circleR)
	ax.add_artist(raza)
	ax.add_artist(punct)
	ax.add_artist(circler)
	ax.add_artist(trace)

	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.draw()

	toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
	toolbar.update()

	canvas.mpl_connect(
	    "key_press_event", lambda event: print(f"you pressed {event.key}"))
	canvas.mpl_connect("key_press_event", key_press_handler)

	canvas.get_tk_widget().grid(column=0, row=0, rowspan=11, sticky='news')

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
	    punct.set_xy([x2-(P/2), y2-(P/2)])
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
	root.mainloop()

def polar():
	global canvas
	if canvas:
	    canvas.get_tk_widget().destroy()

	plt.close('all')

	a = RSize.get()
	b = rSize.get()
	P = primitiveSize.get()

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

	punct = plt.Rectangle((0, 0), P, P, color="b", visible=Var1.get())
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

	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.draw()

	toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
	toolbar.update()

	canvas.mpl_connect(
	    "key_press_event", lambda event: print(f"you pressed {event.key}"))
	canvas.mpl_connect("key_press_event", key_press_handler)

	canvas.get_tk_widget().grid(column=0, row=0, rowspan=11, sticky='news')

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
	tkinter.mainloop()

root = tkinter.Tk()
root.title('Epicycloid Function Visualizer')

canvas = None

root.columnconfigure(0, weight=3)
root.rowconfigure(8, weight=1)

text1 = tkinter.Label(root, text="Размер большей окружности:")
text1.grid(column=1, row=0, sticky='news')
RSize = tkinter.IntVar()
entry_R = tkinter.Entry( root, textvariable=RSize)
RSize.set("32")
entry_R.grid(column=1, row=1, sticky='news')

text2 = tkinter.Label(root, text="Размер малой окружности:")
text2.grid(column=1, row=2, sticky='news')
rSize = tkinter.IntVar()
entry_r = tkinter.Entry( root, textvariable=rSize)
rSize.set("16")
entry_r.grid(column=1, row=3, sticky='news')

Var1 = tkinter.IntVar()
c1 = tkinter.Checkbutton(root, text='Отоброжать примитив',variable=Var1, onvalue=1)
c1.grid(column=1, row=6, sticky='news')

text3 = tkinter.Label(root, text="Размер примитива:")
text3.grid(column=1, row=4)
primitiveSize = tkinter.IntVar()
entry_primitive = tkinter.Entry( root, textvariable=primitiveSize)
primitiveSize.set("2")
entry_primitive.grid(column=1, row=5, sticky='news')

button_c = tkinter.Button(root, text="Обновить график\n(в декартовой системе координат)", command=cartesian)
button_c.grid(column=1, row=9, sticky='news')
button_p = tkinter.Button(root, text="Обновить график\n(в полярной системе координат)", command=polar)
button_p.grid(column=1, row=10, sticky='news')

root.mainloop()
