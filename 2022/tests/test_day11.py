from day11 import Day11


class TestDay11:
    def setup_method(self):
        self.day11 = Day11()
        self.input_path = '../inputs/day11/input_test.txt'

    def test_that_test_input_returns_what_is_given_in_problem_description_part_1(self):
        input = self.day11.parse_input(self.input_path)
        solution = self.day11.part1(input, n_rounds=20)
        assert solution == 10605

    def test_that_test_input_returns_what_is_given_in_problem_description_part_2(self):
        input = self.day11.parse_input(self.input_path)
        solution = self.day11.part2(input, n_rounds=10000)
        assert solution == 2713310158



    def test_parse_input(self):
        monkeys = self.day11.parse_input(self.input_path)
        assert monkeys[0] == {
            'monkey_number': 0,
            'starting_items': [79, 98],
            'operation': ['old', '*', '19'],
            'test': 23,
            'next_monkey_if_test_true': 2,
            'next_monkey_if_test_false': 3
        }

    def test_worry_levels_after_one_round_are_correct(self):
        monkeys = self.day11.parse_input(self.input_path)
        solution = self.day11.part1(monkeys, n_rounds=1)
