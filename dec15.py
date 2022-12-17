# %%
import numpy as np

import time

from utilities.helper_functions import scrape_data

input_test = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

day = 15
input_lst, input_str = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_lst)} lines of data input.")

# %%
def dec15_parser(data):
    data = data.replace('Sensor at x=','').replace(', y=',',').replace(': closest beacon is at x=',',').replace(', y=',',')
    locations = []
    for row in data.split('\n'):
        coords = list(map(int, row.split(',')))
        locations.append([(coords[0], coords[1]), (coords[2], coords[3])])

    return locations

class Sensor():
    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon

        self.s_x = sensor[0]
        self.s_y = sensor[1]
        self.b_x = beacon[0]
        self.b_y = beacon[1]

        # Manhatten distance
        self.beacon_dist = np.abs((self.b_x - self.s_x, self.b_y - self.s_y)).sum()

        # Sensor reachable rows
        self.reachable_rows = range(self.s_y - self.beacon_dist, self.s_y + self.beacon_dist + 1)
    
    def get_row_coverage(self, row):
        # coverage for a given row in
        row_coverage = []
        row_range = self.beacon_dist - np.abs(self.s_y - row)
        row_coverage = [self.s_x + h_dist for h_dist in range(-row_range, +row_range + 1)]
        return row_coverage

    def get_row_coverage_bounds(self, row):
        if row in self.reachable_rows:
            row_range = self.beacon_dist - np.abs(self.s_y - row)
            row_min = self.s_x - row_range
            row_max = self.s_x + row_range
        else:
            row_min = np.nan
            row_max = np.nan
        return row_min, row_max
    
    def get_reachable_rows(self):
        return range(self.s_y - self.beacon_dist, self.s_y + self.beacon_dist + 1)


# %% Part 1
# Parse data coordinates
sensor_coords = dec15_parser(data=input_str)

# initiate sensor instances
sensors = [Sensor(sensor=sensor_pos, beacon=beacon_pos) for sensor_pos, beacon_pos in sensor_coords]

# Find row covered
row = 2000000
rows_covered = set([coverage for sensor in sensors for coverage in sensor.get_row_coverage(row)])
beacons_in_row = set([sensor.b_y for sensor in sensors if sensor.b_y == row])
no_possible_beacon = rows_covered - beacons_in_row
print("Part 1:", len(no_possible_beacon))

#%% Part 2
c_min = 0
c_max = 4000000
row_range = range(c_min, c_max + 1)
stop = False

for row in row_range:
    if stop:
        break

    spans = sorted([sensor.get_row_coverage_bounds(row) for sensor in sensors if row in sensor.reachable_rows])
    row_min = spans[0][0]
    row_max = spans[0][1]

    if row_min > c_min:
        beacon = (row_min - 1, row)
        print(row_min, row_max, sensor_min, sensor_max)
        print(beacon)
        stop = True
        break

    for sensor_min, sensor_max in spans[1:]:
        if (sensor_min <= row_max) & (sensor_max > row_max):
            row_max = sensor_max
        elif row_max >= c_max:
            break
        elif sensor_min > row_max:
            beacon = (row_max + 1, row)
            print(row_min, row_max, sensor_min, sensor_max)
            print(beacon)
            stop = True
            break

answer = 4000000*beacon[0] + beacon[1]
print(f"Part 2:", answer)
