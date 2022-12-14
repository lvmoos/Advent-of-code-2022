# %%
import numpy as np

from utilities.helper_functions import scrape_data, timer_function

#%% Fetch data
input3_test=['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']
input3, input3_txt = scrape_data(day=3)

print(f"Test input:\n{input3_test}")
print(f"Fetched {len(input3)} lines of data input.")

# %% Dec 3 part 1
def dec3_part1(data):
    # Find duplicates
    backpack_compartments = ((set(p[:int(len(p)/2)]), set(p[int(len(p)/2):])) for p in data)
    compartment_duplicates = (''.join(c[0] & c[1]) for c in backpack_compartments)
    # Map letters to scores
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters += letters.upper()
    prio_map = {l:letters.index(l)+1 for l in letters}
    # Sum scores
    priority_score = np.sum([prio_map[d[0]] for d in compartment_duplicates])

    return priority_score

print(f"Part 1:", dec3_part1(data=input3))
timer_function(func=dec3_part1, data=input3, n_run=10)

# %% Part 2
def dec3_part2(data):
    # Find duplicates
    backpacks = [set(p) for p in data]
    n=3
    groups = [backpacks[i:i+n] for i in range(0, len(backpacks), n)]
    group_ids = [''.join(b[0] & b[1] & b[2]) for b in groups]
    # Map letters to scores
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters += letters.upper()
    prio_map = {l:letters.index(l)+1 for l in letters}
    # Sum scores
    priority_score = np.sum([prio_map[d[0]] for d in group_ids])

    return priority_score

print(f"Part 2:", dec3_part2(data=input3))
timer_function(func=dec3_part2, data=input3, n_run=10)