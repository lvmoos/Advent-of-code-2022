# %%
import numpy as np

from utilities.helper_functions import scrape_data, timer_function

#%% Fetch data
input_test = ['A Y', 'B X', 'C Z']
input2_lst, input2_txt = scrape_data(day=2)
print(f"Test input:\n{input_test}")
print(f"Fetched {len(input2_lst)} lines of data input.")

# %% Part 1
def dec2_part_1(data):
    scores_map = {'A X': 4,
                    'A Y': 8,
                    'A Z': 3,
                    'B X': 1,
                    'B Y': 5,
                    'B Z': 9,
                    'C X': 7,
                    'C Y': 2,
                    'C Z': 6,
                    }
    answer =  np.sum([scores_map[r] for r in data])
    return answer

print(f"Part 1: ", dec2_part_1(data=input2_lst))
timer_function(func=dec2_part_1, data=input2_lst, n_run=10)

# %% Part 2
def dec2_part_2(data):
    scores_map = {'A X': 3,
                    'A Y': 4,
                    'A Z': 8,
                    'B X': 1,
                    'B Y': 5,
                    'B Z': 9,
                    'C X': 2,
                    'C Y': 6,
                    'C Z': 7,
                    }
    answer =  np.sum([scores_map[r] for r in data])
    return answer

print(f"Part 1: ", dec2_part_2(data=input2_lst))
timer_function(func=dec2_part_2, data=input2_lst, n_run=10)