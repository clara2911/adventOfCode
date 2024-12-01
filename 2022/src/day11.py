from day11_classes.monkey import Monkey
from utils import read_lines_into_list
import re


class Day11:

    def __init__(self):
        test_input_path = '../inputs/day11/input_test.txt'
        final_input_path = '../inputs/day11/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]


    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            instructions = self.parse_input(input_path)
            # sum_signals = self.part1(instructions)
            crt_output = self.part2(instructions, n_rounds=10000)
            # print(f"Solution 1: {sum_signals}")
            print(f"Solution 2: {crt_output}")

    @staticmethod
    def parse_input(file_path):
        monkeys = []
        current_monkey = {}
        for line in read_lines_into_list(file_path):
            if line.startswith('Monkey'):
                if current_monkey:
                    monkeys.append(current_monkey)
                assert len(re.findall("\d+", line)) == 1
                monkey_number = int(re.findall("\d+", line)[0])
                current_monkey = {'monkey_number': monkey_number}
            elif 'Starting items' in line:
                starting_items = re.findall("\d+", line)
                current_monkey['starting_items'] = []
                for item in starting_items:
                    current_monkey['starting_items'].append(int(item))
            elif 'Operation' in line:
                operation = line.split(' ')[-3:]
                current_monkey['operation'] = []
                for elem in operation:
                    current_monkey['operation'].append(elem)
            elif 'Test' in line:
                line_split = line.split(' ')
                assert ' '.join(line_split[-3:-1]) == 'divisible by'
                current_monkey['test'] = int(line_split[-1])
            elif 'If true' in line:
                current_monkey['next_monkey_if_test_true'] = int(line.split(' ')[-1])
            elif 'If false' in line:
                current_monkey['next_monkey_if_test_false'] = int(line.split(' ')[-1])
            elif line == "":
                pass
            else:
                raise ValueError(f"We don't expect line: {line}")
        monkeys.append(current_monkey)
        return monkeys

    @staticmethod
    def part1(monkey_data, n_rounds=20):
        all_monkey_tests = [17,13,19,7,11,3,2,5]
        # all_monkey_tests = [23, 19, 13, 17]
        monkey_objects = []
        for i, monkey in enumerate(monkey_data):
            monkey_objects.append(Monkey(
                monkey_number=monkey['monkey_number'],
                all_monkey_tests=all_monkey_tests,
                starting_items=monkey['starting_items'],
                operation=monkey['operation'],
                test=monkey['test'],
                next_monkey_if_test_is_true=monkey['next_monkey_if_test_true'],
                next_monkey_if_test_is_false=monkey['next_monkey_if_test_false']
            ))

        for j in range(n_rounds):
            if j==3 or j==4:
                print(f"round {j+1}/{n_rounds}")
            for k, monkey in enumerate(monkey_objects):
                items_to_throw = monkey.turn()
                for next_monkey, items in items_to_throw.items():
                    monkey_objects[next_monkey].receive_items(items)

        inspection_counts = []
        for i, monkey in enumerate(monkey_objects):
            inspection_count = monkey.get_inspection_count()
            inspection_counts.append(inspection_count)
        return sorted(inspection_counts)[-1] * sorted(inspection_counts)[-2]

    @staticmethod
    def part2(monkey_data, n_rounds=1000):
        all_monkey_tests = [17,13,19,7,11,3,2,5] # this for final input
        # all_monkey_tests = [23, 19, 13, 17] # this for test input
        monkey_objects = []
        for i, monkey in enumerate(monkey_data):
            monkey_objects.append(Monkey(
                monkey_number=monkey['monkey_number'],
                all_monkey_tests=all_monkey_tests,
                starting_items=monkey['starting_items'],
                operation=monkey['operation'],
                test=monkey['test'],
                next_monkey_if_test_is_true=monkey['next_monkey_if_test_true'],
                next_monkey_if_test_is_false=monkey['next_monkey_if_test_false']
            ))

        for j in range(n_rounds):
            if j % 100 ==0:
                print(f"round {j+1}/{n_rounds}")
            for k, monkey in enumerate(monkey_objects):
                items_to_throw = monkey.turn(divide_by_3_after_inspect=False)
                for next_monkey, items in items_to_throw.items():
                    monkey_objects[next_monkey].receive_items(items)
        inspection_counts = []
        for i, monkey in enumerate(monkey_objects):
            inspection_count = monkey.get_inspection_count()
            inspection_counts.append(inspection_count)
        return sorted(inspection_counts)[-1] * sorted(inspection_counts)[-2]


if __name__ == '__main__':
    day11 = Day11()
    day11.main()
