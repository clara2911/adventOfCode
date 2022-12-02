from day2 import Day2
from utils import read_lines_into_list_of_lists


class TestDay2:
    def setup_method(self):
        pass

    def test_that_test_input_returns_what_is_given_in_description(self):
        day2_obj = Day2()
        input_path = '../inputs/day2/input_test.txt'
        print(f"\nInput from: {input_path}")
        matches = read_lines_into_list_of_lists(file=input_path)
        total_score_1 = day2_obj.get_solution_1(
            matches=matches
        )
        total_score_2 = day2_obj.get_solution_2(
            matches=matches
        )
        assert total_score_1 == 15
        assert total_score_2 == 12

    def test_score_per_match_list_all_possibilities(self):
        """
        A=rock, B=paper, C=scissors
        X=rock, Y=paper, C=scissors
        A X rock vs rock 1 + 3 = 4
        A Y rock vs paper 2 + 6 = 8
        A Z rock vs scissors 3 + 0 = 3
        B X paper vs rock 1 + 0 = 1
        B Y paper vs paper 2 + 3 = 5
        B Z paper vs scissors 3 + 6 = 9
        C X scissors vs rock 1 + 6 = 7
        C Y scissors vs paper 2 + 0 = 2
        C Z scissors vs scissors 3 + 3 = 6
        """
        day2_obj = Day2()
        input_path = '../inputs/day2/input_test2.txt'
        print(f"\nInput from: {input_path}")
        matches = read_lines_into_list_of_lists(file=input_path)
        scores_per_match = day2_obj.get_scores_per_match(
            matches=matches
        )
        print(f"Total score: {scores_per_match}")
        assert scores_per_match == [4, 8, 3, 1, 5, 9, 7, 2, 6]
