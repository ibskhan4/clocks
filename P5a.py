#!/usr/bin/env python3
# File       : P5a.py
# Description: Analogue clock using Python closure.
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Define your closure here
def clock_hand(r: float):  # do not change this function name and parameter list
    """Function for a clock hand
    Parameters
    ----------
    r : float
        Length of the clock hand
    Returns
    -------
    callable
        Returns the callable closure function.  The returned function takes a
        single floating point argument `theta` and returns a list-like object
        (x, y) for the `x` and `y` Cartesian coordinates of the clock hand
        position.
    """
    # TODO: implement the closure.  Replace the `lambda theta: (0, 0)`
    # expression below with the name of your implemented closure.

    def cart_coords(theta: float):
        x = r * np.cos(theta * np.pi / 180)
        y = r * np.sin(theta * np.pi / 180)
        return (x, y)

    return cart_coords  # replace the lambda with your closure


t = dt.datetime.now()
h = t.hour
m = t.minute
s = t.second


# Specify the length of hour, minute and second hands

r_h, r_m, r_s = 3, 8, 10

### Calculate theta in degrees for each hand based on current time

# Hour hand calculations
hour = clock_hand(r_h)
x_h, y_h = hour(90 - 30*h - (m/2))

# Minute hand calculations
minute = clock_hand(r_m)
x_m, y_m = minute(90 - 6*m)

# Second hand calculations
second = clock_hand(r_s)
x_s, y_s = second(90 - 6*s)

# Initializing the figure. The plan is to generate two different sets of axes; one will be polar so that we can arrange the labels 
# of the clock. The other will be cartesian so we can plot the hands using the calculated cartesian coordinates 
fig = plt.figure()

# Setting the axis limits in [left, bottom, width, height]
rect = [0.1, 0.1, 0.8, 0.8]

# THE CARTESIAN AXES (Used to draw the hands of the clock)
# Setting up the cartesian axes
ax_carthesian  = fig.add_axes(rect)
# Setting up the polar axEs:
ax_polar = fig.add_axes(rect, polar=True, frameon=False)

# Setting up the limits to accomodate all the hands by using the longest one (i.e. second hand) as a reference point 
ax_carthesian.set_xlim(-r_s-1,r_s+1)
ax_carthesian.set_ylim(-r_s-1,r_s+1)

# Plotting the hour hand on the cartesian axes
ax_carthesian.plot([0,x_h], [0,y_h], color="black", linewidth=4)

# Plotting the minute hand on the cartesian axes
ax_carthesian.plot([0,x_m], [0,y_m], color="black", linewidth=2)

# Plotting the second hand on the cartesian axes
ax_carthesian.plot([0,x_s], [0,y_s], color="black", linewidth=1)

# Making the axes invisible to emulate the image of a clock
ax_carthesian.axis('off')

# THE POLAR AXES (Used to draw the circular labels)
# Setting up the polar axes such that the labels stretch/contract with the length of the second hand (and extend slightly outwards)
ax_polar.set_rlim(0,r_s+1)

# Setting up the hour labels 
ax_polar.set_xticks(np.linspace(0, 2*np.pi, 12, endpoint=False))
ax_polar.set_xticklabels(range(1,13))

# Making the ytick labels invisible for clarity and aesthetic purposes
plt.setp(ax_polar.get_yticklabels(), visible=False)

# Making the appropriate directional and shift changes so that the clock labels start with the 12 at top
ax_polar.set_theta_direction(-1)
ax_polar.set_theta_offset(np.pi/3.0)

# Turning the grid off to simulate the image of a clock
ax_polar.grid(False)

plt.savefig('P5a.png', format='png')
plt.show()

