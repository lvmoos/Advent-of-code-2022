# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data, timer_function

input_test = """30373
25512
65332
33549
35390"""

day = 8
input_lst, input_txt = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_txt)} lines of data input.")

# %%
data = np.array([list(map(int, i)) for i in input_test.split('\n')])

tree_diagram = np.zeros(data.shape) # tracks position of visible trees with a '1'
# loop for rotating the array 3 times 90 degrees
for n_rot_90 in range(4):
    data_rotated = np.rot90(data, k=n_rot_90)
    tree_diagram = np.rot90(tree_diagram, k=1*(n_rot_90 > 0))

    # Entire top row is set to vivible as it is an edge
    tree_diagram[0] = 1

    # Loop through all rows,t hat are not the top and bottom ones (as they are edges)
    for row_idx, tree_row in enumerate(data_rotated[1:-1], 1):
        
        # search through tree line up to the tallest tree
        idx_h_max = np.where(tree_row == np.max(tree_row))[0][0]
        for col_idx in range(1, idx_h_max + 1):
            # if all tress to the left are smaller, current is visible
            if all(tree_row[:col_idx] < tree_row[col_idx]):
                tree_diagram[row_idx][col_idx] = 1


print(np.sum(tree_diagram))
# %% Part 1
house_view = np.zeros(data.shape) # tracks position of visible trees with a '1'
for n_rot_90 in range(2):
    data_rotated = np.rot90(data, k=n_rot_90)
    house_view = np.rot90(house_view, k=1*(n_rot_90 > 0))
    for idx_row, row in enumerate(data_rotated):
        print(row)
        for idx_col, col in enumerate(row):
            # look right
            if idx_col==len(row):
                barrier_right = 0
            else:
                check_right = row[idx_col+1:]
                barrier_right = np.where((col >= check_right) == False)[0]
                if len(barrier_right)==0:
                    barrier_right = len(check_right)
                else:
                    barrier_right = barrier_right[0] + 1

            if idx_col==0:
                barrier_left = 0
            else:
                check_left = row[:idx_col]
                barrier_left = np.where((col >= check_left) == False)[-1]
                # print(col,idx_col, check_left, barrier_left)
                if len(barrier_left)==0:
                    barrier_left = len(check_left)
                else:
                    barrier_left = len(check_left) - barrier_left[-1]

            print(col, barrier_left, barrier_right)


