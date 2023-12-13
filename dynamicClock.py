#!/usr/bin/env python3
# File       : dynamicClock.py
# Description: Animated clock
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

    return cart_coords  

# Setting a stop_time for the while loop
stop_time = dt.datetime.now().minute + 1

##### Copying code from 5a so that upon the initial calling of the function, the analog clock still looks as it should. Without this, there would be a brief second-long 
##### pause at the start where the analog clock doesn't look as it should before everything is set up in the while loop

# Specify the length of hour, minute and second hands
r_h, r_m, r_s = 3, 8, 10

# Setting up the time variables
t = dt.datetime.now()
h = t.hour
m = t.minute
s = t.second

# Hour hand calculations
hour = clock_hand(r_h)
x_h, y_h = hour(90 - 30*h - (m/2))

# Minute hand calculations
minute = clock_hand(r_m)
x_m, y_m = minute(90 - 6*m)

# Second hand calculations
second = clock_hand(r_s)
x_s, y_s = second(90 - 6*s)

# Initializing the figure as in 5a 
fig = plt.figure()

# Initializing both axes as in 5a
rect = [0.1, 0.1, 0.8, 0.8]
ax_carthesian  = fig.add_axes(rect)
ax_polar = fig.add_axes(rect, polar=True, frameon=False)

ax_carthesian.axis('off')
ax_polar.grid(False)

# Setting up the limits to accomodate all the hands by using the longest one (i.e. second hand) as a reference point 
ax_polar.set_rlim(0,r_s+1)
ax_carthesian.set_xlim(-r_s-1,r_s+1)
ax_carthesian.set_ylim(-r_s-1,r_s+1)

# Setting up the hour labels 
ax_polar.set_xticks(np.linspace(0, 2*np.pi, 12, endpoint=False))
ax_polar.set_xticklabels(range(1,13))

# Making the ytick labels invisible for clarity and aesthetic purposes
plt.setp(ax_polar.get_yticklabels(), visible=False)

# Making the appropriate directional and shift changes so that the clock labels start with the 12 at top
ax_polar.set_theta_direction(-1)
ax_polar.set_theta_offset(np.pi/3.0)

# Plotting the hour hand on the cartesian axes as of instant of the functional call
ax_carthesian.plot([0,x_h], [0,y_h], color="black", linewidth=4)

# Plotting the minute hand on the cartesian axes as of instant of the functional call
ax_carthesian.plot([0,x_m], [0,y_m], color="black", linewidth=2)

# Plotting the second hand on the cartesian axes as of instant of the functional call
ax_carthesian.plot([0,x_s], [0,y_s], color="black", linewidth=1)


#### WHILE LOOP 

# Setting up the while loop such that the analog clock stops upon the beginning of the next minute (i.e. second hand hitting the next twelve)
while dt.datetime.now().minute < stop_time:
    
    # The clock 'refreshes' every second
    plt.pause(1)

    # Clearing the axes here for each instance of the loop
    ax_polar.clear()
    ax_carthesian.clear()

    # Setting up the time variables
    t = dt.datetime.now()
    h = t.hour
    m = t.minute
    s = t.second

    # Hour hand calculations
    x_h, y_h = hour(90 - 30*h - (m/2))

    # Minute hand calculations
    x_m, y_m = minute(90 - 6*m)

    # Second hand calculations
    x_s, y_s = second(90 - 6*s)

    # Setting the clock up properly again since it was cleared at the beginning of the loop

    # Setting up the limits to accomodate all the hands by using the longest one (i.e. second hand) as a reference point 
    ax_carthesian.set_xlim(-r_s-1,r_s+1)
    ax_carthesian.set_ylim(-r_s-1,r_s+1)

    # Plotting the hour hand on the cartesian axes
    ax_carthesian.plot([0,x_h], [0,y_h], color="black", linewidth=4)

    # Plotting the minute hand on the cartesian axes
    ax_carthesian.plot([0,x_m], [0,y_m], color="black", linewidth=2)

    # Plotting the second hand on the cartesian axes
    ax_carthesian.plot([0,x_s], [0,y_s], color="black", linewidth=1)

    # Making the grids invisible to emulate the image of a clock
    ax_carthesian.axis('off')
    ax_polar.grid(False)

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

    # Using fig.canvas.draw() to update the figure
    fig.canvas.draw()


