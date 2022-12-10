# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data, timer_function

input_test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

day = 9
input_lst, input_str = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_str)} lines of data input.")

# %% Part 1

def move_head(position, direction):
    direction_map = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    (i, j) = np.add(position, direction_map[direction])
    return (i, j)

def move_tail(tail_position, head_position):
    diff = np.subtract(tail_position, head_position)

    if all(np.abs(diff) <= 1):
        tail_position_new = tail_position
    else:
        tail_position_new = np.add(tail_position, -np.sign(diff))

    return tuple(tail_position_new)

data = input_str.split('\n')
i_h = j_h = i_t= j_t = 0
head_positions = [(i_h, j_h)]
tail_positions = [(i_t, j_t)]

for command in data:
    direction, units = command.split(' ')
    for units in range(int(units)):
        head_position_current = head_positions[-1]
        tail_position_current = tail_positions[-1]
        head_position_new = move_head(head_position_current, direction)
        tail_position_new = move_tail(tail_position_current, head_position_new)
        head_positions.append(head_position_new)
        tail_positions.append(tail_position_new)

answer = len(set(tail_positions))
print(f"Part 1:", answer)

# %%
input_test = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
data = input_str.split('\n')
i_h = j_h = i_t= j_t = 0
n_knots = 9
# knot positions at each step, index 0 is the head, index 1 knot 1 etc, 
knot_positions = [[(i_t, j_t),] for _ in range(n_knots+1)]

# Loop over rows of commands
for command in data:
    direction, units = command.split(' ')
    # Loop over individual 1 step moves in a certain direction
    for units in range(int(units)):
        head_position_current = knot_positions[0][-1]
        head_position_new = move_head(head_position_current, direction)
        knot_positions[0].append(head_position_new)
        # Loop over each individual knot segment
        for knot in range(1, 9 + 1):
            head_position_current = knot_positions[knot-1][-1]
            tail_position_current = knot_positions[knot][-1]
            tail_position_new = move_tail(tail_position_current, head_position_current)

            knot_positions[knot].append(tail_position_new)

answer = len(set(knot_positions[-1]))
print(f"Part 2:", answer)