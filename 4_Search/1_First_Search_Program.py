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

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    position = [0, init[0], init[1]]
    visited_list = []
    open_list = [position]
    while [position[1], position[2]] != goal and len(open_list) > 0:
        length = position[0]
        i = position[1]
        j = position[2]
        neighbours = []
        for k in delta:
            loc_i = i + k[0]
            loc_j = j + k[1]
            out_of_bounds = loc_i < 0 or loc_j < 0 or loc_i == len(grid) or loc_j == len(grid[loc_i]) or grid[loc_i][loc_j] == 1
            in_visited_list = [loc_i, loc_j] in visited_list
            in_open_list = [loc_i, loc_j] in [[node[1], node[2]] for node in open_list]
            if out_of_bounds or in_visited_list or in_open_list:
                continue
            open_list.append([length + cost, loc_i, loc_j])
        visited_list.append([i, j])
        open_list.remove(position)
        if len(open_list) > 0:
            position = sorted(open_list)[0]

    if [position[1], position[2]] == goal:
        return position
    else:
        return 'fail'

print search(grid,init,goal,cost)
