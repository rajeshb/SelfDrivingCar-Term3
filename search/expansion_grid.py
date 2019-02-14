#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 01:51:17 2019

@author: rajesh
"""

# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    rows = len(grid)
    cols = len(grid[0])
    used = []
    queue = []
    queue.append([0, init[0], init[1]])
    count = 0
    expand = np.empty((len(grid), len(grid[0])))
    expand.fill(-1)
    expand[init[0]][init[1]] = count
    used.append([init[0], init[1]])
    #print("used:", used)
    while len(queue) > 0:
        item = queue.pop(0)
        g = item[0]
        x = item[1]
        y = item[2]
        #print("item : ", item)
        expand[x][y] = count
        count = count + 1
        if x == goal[0] and y == goal[1]:
            break
        for direction in delta:
            next_pos = np.add([x,y], direction)
            if next_pos[0] < 0 or next_pos[0] > rows-1:
                pass
            elif next_pos[1] < 0 or next_pos[1] > cols-1:
                pass
            elif grid[next_pos[0]][next_pos[1]] != 0:
                pass
            elif [next_pos[0],next_pos[1]] in used:
                pass
            else:
                #print("expand:", expand)
                used.append([next_pos[0], next_pos[1]])
                #print("used:", used)
                queue.append([g+cost, next_pos[0], next_pos[1]])
                #print("queue:", queue)
    return expand

search(grid, init, goal, cost)