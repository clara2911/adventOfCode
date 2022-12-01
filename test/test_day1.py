from day1 import Day1


class TestDay1:
    def setup_method(self):
        pass

    def test_that_test_input_returns_what_is_given_in_description(self):
        solution1, solution2 = Day1.get_solution(
            input_path='../inputs/day1/input_test.txt'
        )
        assert solution1 == 24000
        assert solution2 == 45000
