from day10 import Day10


class TestDay10:
    def setup_method(self):
        self.day10 = Day10()
        self.input_path = '../inputs/day10/input_test.txt'

    def test_that_test_input_returns_what_is_given_in_problem_description_part_1(self):
        instructions = self.day10.parse_input(self.input_path)
        sum_signal_strengths = self.day10.part1(instructions)
        assert sum_signal_strengths == 13140
