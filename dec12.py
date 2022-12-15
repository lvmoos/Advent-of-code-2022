# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data

input_test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

day = 12
input_lst, input_str = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_lst)} lines of data input.")

# %%
def char_val_map(input_grid):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    char_val_map = {letter:i for i, letter in enumerate(letters, 1)}
    char_arr = [list(row) for row in input_grid.split('\n')]
    int_arr = []
    for row in char_arr:
        int_arr.append([char_val_map[letter] for letter in row])

    return int_arr, char_arr

def get_neigbor_nodes(index, grid):
    # No diagonal neighbors
    n_row = len(grid) - 1
    n_col = len(grid[0]) - 1
    x = index[1]
    y = index[0]
    
    neighbors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    neighbors_valid = [i for i in neighbors if (i[0] >= 0) and (i[0] <= n_row) and (i[1] >= 0) and (i[1] <= n_col)]
    
    return neighbors_valid

def get_neighbor_cost(position_current, position_neighbor, grid):
    value_current = grid[position_current[0]][position_current[1]]
    value_neighbor = grid[position_neighbor[0]][position_neighbor[1]]
    cost = 1*(value_neighbor > value_current + 1)

    return cost

def get_valid_neighbors(position_current, grid):
    neighbors = get_neigbor_nodes(index=position_current, grid=grid)
    neighbors = [n for n in neighbors if get_neighbor_cost(position_current=position_current, position_neighbor=n, grid=grid) == 0]
    return neighbors

def Dijkstra(graph, source, target):
    Q = set()
    dist = {}
    prev = {}
    for idx_row, row in enumerate(graph):
        for idx_col, col in enumerate(row):
            v = (idx_row, idx_col)
            dist[v] = np.inf
            prev[v] = np.nan
            Q.add(v)

    dist[source] = 0

    while len(Q) > 0:
        dist_search = [d for d in dist if d in Q]
        u = min(dist_search, key=dist.get)
        Q.remove(u)

        # Use this in Part 1 to stop at E. Ignores in Part 2, because now start here and find dist to all nodes
        # if u == target:
        #     print(f'Found target {u} with steps {dist[u]}')
        #     dist[u] = alt + 1
        #     break

        neighbors = get_valid_neighbors(position_current=u, grid=graph)
        neighbors_in_Q = [n for n in neighbors if n in Q]
        for n in neighbors_in_Q:
            alt =  dist[u] + 1
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u

    return dist, prev, Q

# %% Part 1
data = input_str

n_col = len(data.split('\n')[0])
idx_S = data.replace('\n','').index('S') + 1
idx_E = data.replace('\n','').index('E') + 1
start = (idx_S // n_col, idx_S % n_col - 1)
target = (idx_E // n_col, idx_E % n_col - 1)

data = data.replace('S', 'a').replace('E', 'z')

number_grid, char_grid = char_val_map(data)

dist, prev, Q = Dijkstra(graph=number_grid, source=start, target=target)

#%% Part 2
grid_reversed = np.abs(np.add(number_grid, -27))
dist, prev, Q = Dijkstra(graph=grid_reversed, source=target, target=None)
targets = []
for idx_row, row in enumerate(grid_reversed):
    for idx_col, col in enumerate(row):
        if grid_reversed[idx_row][idx_col] == 26:
            targets.append((idx_row, idx_col))

paths = [dist[target] for target in targets]
print(f"Answer: minimum steps in {len(paths)} paths is {min(paths)}")
