import re
from utils import read_lines_into_list


class Day5:

    def __init__(self):
        test_input_path = '../inputs/day05/input_test_moves_only.txt'
        final_input_path = '../inputs/day05/input_moves_only.txt'
        self.all_input_paths = [test_input_path, final_input_path]

    def main(self):

        for input_type, input_path in zip(["test", "final"], self.all_input_paths):
            print(f"\nInput from: {input_path}")
            instruction_list = self.parse_input(input_path)
            top_crates = self.part1(instruction_list=instruction_list, input_type=input_type)
            top_crates_2 = self.part2(instruction_list=instruction_list, input_type=input_type)
            print(f"Solution 1: {top_crates}")
            print(f"Solution 2: {top_crates_2}")



    def parse_input(self, input_path):
        instruction_list = []
        lines = read_lines_into_list(input_path)
        for line in lines:
            instruction = re.findall("\d+", line)
            instruction = [int(num) for num in instruction]
            instruction[1:] = [num-1 for num in instruction[1:]]  # start stack numbers at 0 instead of 1
            instruction_list.append(instruction)
        return instruction_list

    def part1(self, instruction_list, input_type="test"):
        stacks = self.reset_stacks(stack_type=input_type)
        for instruction in instruction_list:
            n_crates = instruction[0]
            start_stack = instruction[1]
            end_stack = instruction[2]
            for i in range(n_crates):
                crate = stacks[start_stack].pop()
                stacks[end_stack].append(crate)
        top_crates = ''.join([stack[-1] for stack in stacks])
        return top_crates

    def part2(self, instruction_list, input_type="test"):
        stacks = self.reset_stacks(stack_type=input_type)
        for instruction in instruction_list:
            n_crates = instruction[0]
            start_stack = instruction[1]
            end_stack = instruction[2]
            crates = stacks[start_stack][-n_crates:]
            stacks[start_stack] = stacks[start_stack][:-n_crates]
            stacks[end_stack] += crates
        top_crates = ''.join([stack[-1] for stack in stacks])
        return top_crates

    def reset_stacks(self, stack_type):
        if stack_type == "test":
            stacks = self.get_test_stacks()
        else:
            stacks = self.get_final_stacks()
        return stacks

    def get_test_stacks(self):
        stacks = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]
        return stacks

    def get_final_stacks(self):
        stacks = [
            ['S', 'L', 'W'],
            ['J', 'T', 'N', 'Q'],
            ['S', 'C', 'H', 'F', 'J'],
            ['T', 'R', 'M', 'W', 'N', 'G', 'B'],
            ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B'],
            ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L'],
            ['D', 'W', 'R', 'N', 'J', 'M'],
            ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J'],
            ['H', 'L', 'Q', 'N', 'B', 'F', 'T']
        ]
        return stacks


if __name__ == '__main__':
    day5_obj = Day5()
    day5_obj.main()
