#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:59:13 2017

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
# If there is no valid path f   rom the start point
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
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
        
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right
         
delta_name = ['^', '<', 'v', '>']

def get_next_moves(grid, pos):
    next_moves = []
    for i in range(len(delta)):
        next_move = np.add(pos, delta[i])
        if next_move[0] >= 0 and next_move[1] >= 0 and next_move[0] < len(grid) and next_move[1] < len(grid[1]):
            next_moves.append(next_move)
    return next_moves

def get_valid_moves(grid, pos):
    moves = get_next_moves(grid, pos)
    valid_moves = []
    for i in range(len(moves)):
        if grid[moves[i][0]][moves[i][1]] == 0:
            valid_moves.append(moves[i])
    return valid_moves

def get_value(list_data, row, col):
    for item in list_data:
        if item[0] == row and item[1] == col:
            return item[2]
    return False

def update_list(list_data, row, col, value):
    for item in list_data:
        if item[0] == row and item[1] == col:
            item[2] = value
            break

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path = "fail"
    result = []
    flag = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if init[0] == i and init[1] == j:
                flag = True
            else:
                flag = False
            result.append ([i, j, flag])

    current_pos = init
    path_list = []
    q_value = 0
    path_list.append([q_value, init[0], init[1]])
    
    while len(path_list) > 0:
        current_item = path_list[np.argmin(path_list, axis=0)[0]]        
        q_value = current_item[0] + 1
        current_pos = [current_item[1], current_item[2]]
        update_list(result, current_item[1], current_item[2], True)
        del path_list[np.argmin(path_list, axis=0)[0]]
        valid_moves = get_valid_moves(grid, current_pos)

        for i in range(len(valid_moves)):
            if get_value(result, valid_moves[i][0], valid_moves[i][1]) != True:
                path_list.append([q_value, valid_moves[i][0], valid_moves[i][1]])
                update_list(result, valid_moves[i][0], valid_moves[i][1], True)

        for item in path_list:
            if item[1] == goal[0] and item[2] == goal[1]:
                path = item
                break
            
    return path
    
ret = search(grid, init, goal, cost)

print(ret)