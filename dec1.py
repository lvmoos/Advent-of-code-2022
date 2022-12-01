# %%
import numpy as np

from utilities.helper_functions import scrape_data, timer_function

#%% Fetch data
input_1_test="""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

input_1, input_txt = scrape_data(day=1)

print(f"Test input:\n{input_1_test}")
print(f"Fetched {len(input_1)} lines of data input.")

# %% Part 1
# Part 1 - Sum calories pr elf
def dec1_part_1(data):
    elf_calories = sorted([np.sum(list(map(int, elf.split('\n')))) for elf in data.split('\n\n')])
    
    return elf_calories

elf_calories = dec1_part_1(data=input_txt)

print(f"Part 1: Maximum calories carried by one elf: {elf_calories[-1]}")
timer_function(func=dec1_part_1, data=input_txt, n_run=10)

# Part 2
top3 = elf_calories[-3:]
print(f"Part 2: Maximum calories carried by top 3 elves({top3}): {np.sum(top3)}")
timer_function(func=dec1_part_1, data=input_txt, n_run=10)
# %%
