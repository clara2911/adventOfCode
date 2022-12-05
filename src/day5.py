import re
from utils import read_lines_into_list


class Day5:

    def __init__(self):
        """
            [D]
        [N] [C]
        [Z] [M] [P]
        1   2   3

        """



    def main(self):
        test_input_path = '../inputs/day5/input_test_moves_only.txt'
        final_input_path = '../inputs/day5/input_moves_only.txt'
        for input_path in [test_input_path, final_input_path]:
            print(f"\nInput from: {input_path}")
            if input_path == test_input_path:
                stacks = self.get_test_stacks()
            else:
                stacks = self.get_final_stacks()
            instruction_list = self.parse_input(input_path)

            top_crates = self.get_solution_1(instruction_list=instruction_list, stacks=stacks)
            if input_path == test_input_path:
                stacks = self.get_test_stacks()
            else:
                stacks = self.get_final_stacks()
            top_crates_2 = self.get_solution_2(instruction_list=instruction_list, stacks=stacks)
            print(f"Solution 1: {top_crates}")
            print(f"Solution 2: {top_crates_2}")

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

    def parse_input(self, input_path):
        instruction_list = []
        lines = read_lines_into_list(input_path)
        for line in lines:
            instruction = re.findall("\d+", line)
            instruction = [int(num) for num in instruction]
            instruction[1:] = [num-1 for num in instruction[1:]]  # start stack numbers at 0 instead of 1
            instruction_list.append(instruction)
        return instruction_list

    def get_solution_1(self, instruction_list, stacks):
        for instruction in instruction_list:
            # print(f"instruction {instruction}")
            n_crates = instruction[0]
            start_stack = instruction[1]
            end_stack = instruction[2]
            for i in range(n_crates):
                crate = stacks[start_stack].pop()
                stacks[end_stack].append(crate)

        top_crates = ''.join([stack[-1] for stack in stacks])
        return top_crates

    def get_solution_2(self, instruction_list, stacks):
        for instruction in instruction_list:
            # print(stacks)
            # print(instruction)
            n_crates = instruction[0]
            start_stack = instruction[1]
            end_stack = instruction[2]
            crates = stacks[start_stack][-n_crates:]
            # print(f"n_crates: {n_crates},, crates: {crates}")
            stacks[start_stack] = stacks[start_stack][:-n_crates]
            stacks[end_stack] += crates
        #     print("After:")
        # print(stacks)
        top_crates = ''.join([stack[-1] for stack in stacks])
        return top_crates


if __name__ == '__main__':
    day5_obj = Day5()
    day5_obj.main()
