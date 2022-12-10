# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data, timer_function

input_test = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

day = 10
input_lst, input_str = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_str)} lines of data input.")

# %% Part 1
data_input = input_str
adder_cycles = data_input.replace('noop', '0').replace('\naddx ', '\n0\n').replace('addx ', '0\n').split('\n')
# values at the start of each cycle: 
#   one is added to all cumulatative values to account for starting value of 1
#   1 is inserted at the start to offset cycles values to match start of cycle instead of end
start_cycle_values = np.insert(np.add(np.cumsum([int(i) for i in adder_cycles]), 1), 0, 1)

check_cycles = [20, 60, 100, 140, 180, 220]
signal_strength_sum = np.sum([cycle*(start_cycle_values[cycle-1]) for cycle in check_cycles])
print(f"Part 1:", signal_strength_sum)

# %% Part 2
draw_str = ''
for pixel in range(40*6+1):
    sprite_position = start_cycle_values[pixel]
    if np.mod(pixel, 40) in (sprite_position - 1, sprite_position, sprite_position + 1):
        draw_str += '#'
    else:
        draw_str += ' '

print(np.array([draw_str[40*line:40*(line+1)] for line in range(6)]))