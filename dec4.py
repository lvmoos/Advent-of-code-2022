# %%
import numpy as np

from utilities.helper_functions import scrape_data, timer_function

#%% Fetch data
input4_test=['2-4,6-8',
'2-3,4-5',
'5-7,7-9',
'2-8,3-7',
'6-6,4-6',
'2-6,4-8']

input4, input4_txt = scrape_data(day=4)

print(f"Test input:\n{input4_test}")
print(f"Fetched {len(input4)} lines of data input.")

# %% Dec 3 part 1
def dec4_part1(data):
    pairs = [list(map(int, p.replace('-',',').split(','))) for p in data]
    pair_overlaps = [1 if (p[0]>=p[2] and p[1]<=p[3]) or (p[2]>=p[0] and p[3]<=p[1])
     else 0 for p in pairs]

    answer = np.sum(pair_overlaps)
    return answer


print(f"Part 1:", dec4_part1(data=input4))
timer_function(func=dec4_part1, data=input4, n_run=10)
# %% Part 2
def dec4_part2(data):
    pairs = [list(map(int, p.replace('-',',').split(','))) for p in data]
    pair_overlaps_partial = [1 if (p[1]>=p[2] and p[1]<=p[3]) or (p[3]>=p[0] and p[3]<=p[1])
     else 0 for p in pairs]

    answer = np.sum(pair_overlaps_partial)
    return answer

print(f"Part 2:", dec4_part2(data=input4))
timer_function(func=dec4_part2, data=input4, n_run=10)