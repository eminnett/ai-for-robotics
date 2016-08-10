# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def cells_with_value(value_grid, value):
    cells = []
    for i in xrange(len(value_grid)):
        for j in xrange(len(value_grid[i])):
            if value_grid[i][j] == value:
                cells.append([i,j])
    return cells

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value_grid = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    cost = 0
    value_grid[goal[0]][goal[1]] = cost
    counter = 0
    edge = [goal]
    while len(edge) > 0 and counter < 100:
        counter += 1
        cost += 1
        for cell in edge:
            for k in delta:
                i = cell[0] + k[0]
                j = cell[1] + k[1]
                if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]) or grid[i][j] == 1:
                    continue
                if value_grid[i][j] > cost:
                    value_grid[i][j] = cost

        edge = cells_with_value(value_grid, cost)


    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value_grid

print compute_value(grid,goal,cost)
