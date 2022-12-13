# %%
import numpy as np
import time

from utilities.helper_functions import scrape_data, timer_function

input_test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

day = 11
input_lst, input_str = scrape_data(day=day)

print(f"Test input:\n{input_test}")
print(f"Fetched {len(input_lst)} lines of data input.")

# %% Data parsing
def parse_monkey_data(data):
    data_input = data.split('\n')
    monkeys_dct = {}
    for row in data_input:
        if 'Monkey' in row:
            monkey_num = int(row.split(' ')[1][:-1])
            monkeys_dct[monkey_num] = {}
        elif 'Starting items' in row:
            monkeys_dct[monkey_num]['items'] = [int(n) for n in row.split(': ')[-1].split(', ')]
        elif 'Operation' in row:
            operator, operator_value = row.replace('* old', '** 2').split('= old ')[-1].split(' ')
            monkeys_dct[monkey_num]['operator'] = operator
            monkeys_dct[monkey_num]['operator_value'] = int(operator_value)
        elif 'Test' in row:
            monkeys_dct[monkey_num]['test_divisor'] = int(row.split('by ')[-1])
        elif 'If true' in row:
            monkeys_dct[monkey_num]['true_action'] = int(row.split('throw to monkey ')[-1])
        elif 'If false' in row:
            monkeys_dct[monkey_num]['false_action'] = int(row.split('throw to monkey ')[-1])

    return monkeys_dct

# %%
class MonkeyClass:
    def __init__(self, items, operator, operator_value, test_divisor, true_action, false_action, monkey_tests):
        self.items = items
        self.operator = operator
        self.operator_value = operator_value
        self.test_divisor = test_divisor
        self.true_action = true_action
        self.false_action = false_action
        self.monkey_tests = monkey_tests

        self.inspection_count = 0

    def receive_item(self, item):
        self.items.append(item)

    def inspect_item(self, item):
        item_value_new = eval(f"{item}{self.operator}{self.operator_value}")
        return item_value_new
    
    def test_item(self, item):
        if item % self.test_divisor == 0:
            pass_to_monkey = self.true_action
        else:
            pass_to_monkey = self.false_action
        
        return pass_to_monkey

    def reduce_worry(self, item):
        # reduced_worry = item // 3
        reduced_worry = item % self.monkey_tests
        return reduced_worry

    def item_turn(self, item):
        new_inspect_value = self.inspect_item(item = item)
        new_test_value = self.reduce_worry(item = new_inspect_value)
        pass_monkey = self.test_item(item = new_test_value)

        return {'item': new_test_value, 'pass_to': pass_monkey}

    def monkey_turn(self):
        item_actions = []
        for item in self.items:
            action = self.item_turn(item)
            item_actions.append(action)

        return item_actions

    def execute_turn(self):
        item_actions = self.monkey_turn()
        self.inspection_count += len(item_actions)
        self.items = []

        return item_actions


# % instantiate list of monkey class objects
monkeys_dct = parse_monkey_data(data=input_str)
monkey_tests = np.product([items['test_divisor'] for _, items in monkeys_dct.items()])
monkeys_ini = []
for monkey in monkeys_dct.values():
    m = MonkeyClass(
        items=monkey['items'],
        operator=monkey['operator'],
        operator_value=monkey['operator_value'],
        test_divisor=monkey['test_divisor'],
        true_action=monkey['true_action'],
        false_action=monkey['false_action'],
        monkey_tests=monkey_tests
        )
    monkeys_ini.append(m)


# %% Part 1
n_rounds = 10000

monkeys = monkeys_ini
for round in range(1, n_rounds + 1):
    for monkey_num, monkey in enumerate(monkeys):
        actions = monkey.execute_turn()
        for action in actions:
            monkeys[action['pass_to']].receive_item(action['item'])

inspection_count = [monkey.inspection_count for monkey in monkeys]
answer = np.product(sorted(inspection_count)[-2:])
print(inspection_count)
print(f"Part 1:", answer)