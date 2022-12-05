from day5 import Day5


class TestDay5:
    def setup_method(self):
        self.day5_obj = Day5()
        self.input_path = '../inputs/day5/input_test_moves_only.txt'

    def test_that_test_input_returns_what_is_given_in_description_part_1(self):
        instruction_list = self.day5_obj.parse_input(self.input_path)
        top_crates = self.day5_obj.get_solution_1(instruction_list=instruction_list)
        assert top_crates == 'CMZ'
