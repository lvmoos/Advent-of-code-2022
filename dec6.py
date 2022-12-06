# %%
import numpy as np

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
print(f"Part 1:", dec6_part1(data=input_txt, marker_length = 14))