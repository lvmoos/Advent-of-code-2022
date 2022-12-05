# %%
import numpy as np

from utilities.helper_functions import scrape_data, timer_function

#%% Fetch data
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
position_ini_test=['ZN', 'MCD', 'P']
input5_test=['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1','move 1 from 1 to 2']

input5_lst, input5_txt = scrape_data(day=5)
position_ini = ['TVJWNRMS', 'VCPQJDWB', 'PRDHFJB', 'DNMBPRF', 'BTPRVH', 'TPBC', 'LPRJB', 'WBZTLSCN','GSL']
position_ini = [stack[::-1] for stack in position_ini]
input5_lst = input5_lst[8+2:]

print(f"Test input:\n{input5_test}")
print(f"Fetched {len(input5_lst)} lines of data input.")

# %% Dec 3 part 1
def dec5_part1(data, position_ini):
    moves = [list(map(int,move.replace('move ','').replace(' from ', ',').replace(' to ', ',').split(','))) for move in data]
    position = position_ini.copy()

    for n_crates, stack_start, stack_end in moves:
        idx_i = stack_start - 1
        idx_f = stack_end - 1

        # Crate by crate - REverse order of slice
        moved_crates = position[idx_i][-n_crates:][::-1]
        position[idx_i] = position[idx_i][:len(position[idx_i])-n_crates]
        position[idx_f] += moved_crates


    answer = ''.join([stack[-1] for stack in position])

    return answer

print(f"Part 1:", dec5_part1(data=input5_lst, position_ini=position_ini))

# %% Part 2
def dec5_part2(data, position_ini):
    moves = [list(map(int,move.replace('move ','').replace(' from ', ',').replace(' to ', ',').split(','))) for move in data]
    position = position_ini.copy()

    for n_crates, stack_start, stack_end in moves:
        idx_i = stack_start - 1
        idx_f = stack_end - 1

        # all crates at once
        moved_crates = position[idx_i][-n_crates:]
        position[idx_i] = position[idx_i][:len(position[idx_i])-n_crates]
        position[idx_f] += moved_crates


    answer = ''.join([stack[-1] for stack in position])

    return answer

print(f"Part 2:", dec5_part2(data=input5_lst, position_ini=position_ini))