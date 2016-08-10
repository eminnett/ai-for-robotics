# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right

goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    state = init
    counter = 0

    def position_is_legal(grid, x, y):
        return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]) and grid[y][x] == 0

    # TODO: Address this problem using the 4D Value Function, not the recursion method I initially attempted.
    def optimal_action(grid, state, goal, base_cost, total_cost):
        cost_boundary = 99
        lowest_cost = cost_boundary
        optimal_action_index = 0
        new_state = state
        for a in xrange(len(action)):
            accumulated_cost = 0
            new_direction = (state[2] + action[a]) % len(forward)
            move = forward[new_direction]
            y = state[0] + move[0]
            x = state[1] + move[1]
            if position_is_legal(grid, x, y):
                if [y, x] == goal:
                    accumulated_cost = total_cost[a]
                else:
                    total_cost = [(c + base_cost[a]) for c in total_cost]
                    if max(total_cost) < cost_boundary:
                        _a, accumulated_cost, _ = optimal_action(grid, [y, x, new_direction], goal, base_cost, total_cost)
                    else:
                        accumulated_cost = cost_boundary

                if accumulated_cost < lowest_cost:
                    lowest_cost = accumulated_cost
                    optimal_action_index = a
                    new_state = [y, x, new_direction]

        return optimal_action_index, lowest_cost, new_state

    while [state[0], state[1]] != goal and counter < 100:
        counter += 1
        a, action_cost, new_state = optimal_action(grid, state, goal, cost, cost)
        policy2D[state[0]][state[1]] = action_name[a]
        state = new_state

    policy2D[goal[0]][goal[1]] = '*'
    return policy2D

print optimum_policy2D(grid,init,goal,cost)
