from utils import read_lines_into_list


class Day6:

    def __init__(self):
        self.test_input_path = '../inputs/day6/input_test.txt'
        self.final_input_path = '../inputs/day6/input.txt'
        self.all_input_paths = [self.test_input_path, self.final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            instruction_list = self.parse_input(input_path)
            top_crates = self.part1(instruction_list=instruction_list, stacks=3)
            top_crates_2 = self.part2(instruction_list=instruction_list, stacks=4)
            print(f"Solution 1: {top_crates}")
            print(f"Solution 2: {top_crates_2}")

    def parse_input(self, input_path):
        return 4

    def part1(self, instruction_list, stacks):
        return 5

    def part2(self, instruction_list, stacks):
        return 6


if __name__ == '__main__':
    day6_obj = Day6()
    day6_obj.main()
