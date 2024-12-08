from day06.day08 import Day6


class TestDay6:
    def setup_method(self):
        self.day6_obj = Day6()
        self.input_path = '../inputs/day06/input_test.txt'

    def test_that_test_input_returns_what_is_given_in_description_part_1(self):
        datastream = self.day6_obj.parse_input(self.input_path)
        n_processed_chars = self.day6_obj.get_char_count_before_n_different(datastream, n_different=4)
        assert n_processed_chars == 11

    def test_that_test_input_returns_what_is_given_in_description_part_2(self):
        datastream = self.day6_obj.parse_input(self.input_path)
        n_processed_chars = self.day6_obj.get_char_count_before_n_different(datastream, n_different=14)
        assert n_processed_chars == 26
