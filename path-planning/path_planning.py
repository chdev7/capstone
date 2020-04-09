import matplotlib.pyplot as plt
import math
import numpy as np
from astar import AStarPlanner

#set start point
x_initial = 0
y_initial = 0

#set end point 
x_goal = 45
y_goal = 50

#set step size and calculate the number of steps to move up
step_size = 5
n_step = int(y_goal/step_size)+1

point_x, point_y = [], []

for i in range(n_step):
    add_step = i*step_size
    if i%2 == 0:
        point_x.append(x_initial)
        point_y.append(add_step)
        point_x.append(x_goal)
        point_y.append(add_step)
    elif i%2 != 0:
        point_x.append(x_goal)
        point_y.append(add_step)
        point_x.append(x_initial)
        point_y.append(add_step)

robot_radius = 2.0
grid_size = 2.0

# set obstable positions
ox, oy = [], []
for i in range(20, 41):
    ox.append(i)
    oy.append(20)
for i in range(20, 41):
    ox.append(20.0)
    oy.append(i)
for i in range(20, 41):
    ox.append(i)
    oy.append(40.0)
for i in range(20, 41):
    ox.append(40.0)
    oy.append(i)   
for i in range(-10, 60):
    ox.append(i)
    oy.append(-10.0)
for i in range(-10, 60):
    ox.append(60.0)
    oy.append(i)
for i in range(-10, 61):
    ox.append(i)
    oy.append(60.0)
for i in range(-10, 61):
    ox.append(-10.0)
    oy.append(i)
    

a_star = AStarPlanner(ox, oy, grid_size, robot_radius)

for i in range(0, len(point_x) - 1):
    plt.grid(True)
    plt.plot(ox, oy, ".k")
    plt.plot(point_x[i], point_y[i], "og")
    plt.plot(point_x[i+1], point_y[i+1], "xb")
    rx, ry = a_star.planning(point_x[i], point_y[i], point_x[i+1], point_y[i+1])
    plt.plot(rx, ry, "-r")
    plt.show()




