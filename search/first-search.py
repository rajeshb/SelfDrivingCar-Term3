#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:53:14 2019

@author: rajesh
"""

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0]]
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
    path = "fail"
    while len(queue) > 0:
        item = queue.pop(0)
        g = item[0]
        x = item[1]
        y = item[2]
        #print("item : ", item)
        if x == goal[0] and y == goal[1]:
            path = item
            break
        used.append([x, y])
        for direction in delta:
            next_pos = np.add([x,y], direction)
            if next_pos[0] < 0 or next_pos[0] > rows-1:
                continue
            if next_pos[1] < 0 or next_pos[1] > cols-1:
                continue
            if grid[next_pos[0]][next_pos[1]] != 0:
                continue
            if [next_pos[0],next_pos[1]] in used:
                continue
            queue.append([g+1, next_pos[0], next_pos[1]])
        #print("queue: ", queue)
    return path

search(grid, init, goal, cost)