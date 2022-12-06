# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data, timer_function

#%% Fetch data
day = 6
input_test='bvwbjplbgvbhsrlpgdmjqwftvncz'
input_lst, input_txt = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_txt)} lines of data input.")

# %% Part 1
def dec6_part1(data, marker_length):
    answer = 'No solution'
    for i in range(0, len(data) - marker_length):
        if len(set(data[i:i + marker_length])) == marker_length:
            answer = i + marker_length
            break

    return answer

print(f"Part 1:", dec6_part1(data=input_txt, marker_length = 4))

# %% Part 2
print(f"Part 2:", dec6_part1(data=input_txt, marker_length = 14))

# %% Non-set/np.unique solution
def dec6_part1_no_set(data, marker_length):
    for i in range(0, len(data) - marker_length):
        marker_batch = data[i:i+marker_length]
    
        for idx, char in enumerate(marker_batch[:-1], 1):
            if char in marker_batch[idx:]:
                duplicate = True
                break
            else:
                duplicate = False
        
        if not duplicate:
            answer = i + marker_length
            break

    return answer

n = 1000
t0 = time.time()
[dec6_part1(input_txt, 14) for _ in range(n)]
t_set = (time.time() - t0)/n
print(f"{t_set}s to complete solution using set()")
t0 = time.time()
[dec6_part1_no_set(input_txt, 14) for _ in range(n)]
t_no_set = (time.time() - t0)/n
print(f"{t_no_set}s to complete solution not using set()")
print(f"{100*(t_no_set-t_set)/t_set:.2f}% computation time change not using set")
# %%
