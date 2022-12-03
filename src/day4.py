from utils import read_lines_into_list
from utils import read_lines_of_strings_into_list_of_lists


class Day4:

    def __init__(self):
        pass

    def main(self):
        test_input_path = '../inputs/day4/input_test.txt'
        final_input_path = '../inputs/day4/input.txt'
        for input_path in [test_input_path, final_input_path]:
            print(f"\nInput from: {input_path}")
            bag_contents = read_lines_of_strings_into_list_of_lists(input_path)
            sum_priorities_1 = self.get_solution_1(bag_contents=bag_contents)
            sum_priorities_2 = self.get_solution_2(bag_contents=bag_contents)
            print(f"Solution 1: {sum_priorities_1}")
            print(f"Solution 2: {sum_priorities_2}")

    def get_solution_1(self, bag_contents):
        return 4

    def get_solution_2(self, bag_contents):
        return 3

if __name__ == '__main__':
    day3_obj = Day4()
    day3_obj.main()
