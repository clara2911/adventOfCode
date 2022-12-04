from day4 import Day4
from utils import read_lines_into_list_of_lists


class TestDay4:
    def setup_method(self):
        self.day4_obj = Day4()
        self.input_path = '../inputs/day4/input_test.txt'
        self.input_path2 = '../inputs/day4/input_test2.txt'
        self.input_path_full = '../inputs/day4/input.txt'

    def test_that_test_input_returns_what_is_given_in_description_part_1(self):
        lines = read_lines_into_list_of_lists(file_path=self.input_path, sep=',')
        cleaning_pairs = [[elf.split('-') for elf in line] for line in lines]
        num_containing_pairs = self.day4_obj.part1(
            cleaning_pairs=cleaning_pairs
        )
        assert num_containing_pairs == 2

    def test_that_test_input_returns_what_is_given_in_description_part_1_extra_test(self):
        lines = read_lines_into_list_of_lists(file_path=self.input_path2, sep=',')
        cleaning_pairs = [[elf.split('-') for elf in line] for line in lines]
        num_containing_pairs = self.day4_obj.part1(
            cleaning_pairs=cleaning_pairs
        )
        assert num_containing_pairs == 4

    def test_that_full_input_returns_what_is_correct_part_1(self):
        lines = read_lines_into_list_of_lists(file_path=self.input_path_full, sep=',')
        cleaning_pairs = [[elf.split('-') for elf in line] for line in lines]
        num_containing_pairs = self.day4_obj.part1(
            cleaning_pairs=cleaning_pairs
        )
        assert num_containing_pairs == 490

    def test_that_test_input_returns_what_is_given_in_description_part_2(self):
        lines = read_lines_into_list_of_lists(file_path=self.input_path, sep=',')
        cleaning_pairs = [[elf.split('-') for elf in line] for line in lines]
        num_containing_pairs = self.day4_obj.part2(
            cleaning_pairs=cleaning_pairs
        )
        assert num_containing_pairs == 4

