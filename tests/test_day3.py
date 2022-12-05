from day3 import Day3
from utils import read_lines_of_strings_into_list_of_chars


class TestDay3:
    def setup_method(self):
        self.day3_obj = Day3()
        self.input_path = '../inputs/day3/input_test.txt'

    def test_that_test_input_returns_what_is_given_in_description_part_1(self):
        bag_contents = read_lines_of_strings_into_list_of_chars(file_path=self.input_path)
        sum_priorities_1 = self.day3_obj.get_solution_1(
            bag_contents=bag_contents
        )
        assert sum_priorities_1 == 157

    def test_that_test_input_returns_what_is_given_in_description_part_2(self):
        bag_contents = read_lines_of_strings_into_list_of_chars(file_path=self.input_path)
        sum_priorities_2 = self.day3_obj.get_solution_2(
            bag_contents=bag_contents
        )
        assert sum_priorities_2 == 70
