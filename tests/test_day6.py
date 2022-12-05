from day6 import Day6


class TestDay6:
    def setup_method(self):
        self.day6_obj = Day6()
        self.input_path = '../inputs/day6/input_test.txt'

    def test_that_test_input_returns_what_is_given_in_description_part_1(self):
        x = self.day6_obj.parse_input(self.input_path)
        y = self.day6_obj.part1(x, x)
        assert y
