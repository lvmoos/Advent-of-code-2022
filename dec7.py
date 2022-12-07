# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data, timer_function

input_test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

day = 7
input_lst, input_txt = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_txt)} lines of data input.")

# %%
data = input_txt.split('\n')
data = input_lst
file_dirs = {}

sub_dirs = ['/']
for l in data[1:]:
    # print(l)
    if l == '$ cd ..':
        sub_dirs.pop()
    elif '$ cd ' in l:
        sub_dirs.append(l[5:])
    elif l[0].isnumeric():
        file_dirs[l] = ['_'.join(sub_dirs[:i]) for i in range(1, len(sub_dirs)+1)]
    else:
        pass

dir_sizes = {}
for file, directories in file_dirs.items():
    file_size = int(file.split(' ')[0])
    for dir in directories:
        dir_sizes[dir] = dir_sizes.get(dir, 0) + file_size


max_size = 100000

answer = np.sum([d for d in dir_sizes.values() if d <= max_size])
print([(d,s) for s,d in dir_sizes.items() if d <= max_size])
print(answer)

# %%
max_capacity = 70000000
req_capacity = 30000000

used_capacity = dir_sizes['/']
missing_capacity = req_capacity - (max_capacity - used_capacity)
size_sorted = np.array(sorted([d for d in dir_sizes.values()])) 
min_size = size_sorted[size_sorted >= missing_capacity][0]

