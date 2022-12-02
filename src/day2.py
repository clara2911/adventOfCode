from utils import read_lines_into_list


class Day2:

    def __init__(self):
        pass

    def main(self):
        test_input_path = '../inputs/day2/input_test.txt'
        final_input_path = '../inputs/day2/input.txt'
        for input_path in [test_input_path, final_input_path]:
            total_score_1 = self.get_solution_1(input_path=input_path)
            total_score_2 = self.get_solution_2(input_path=input_path)
            print(f"Solution 1: Total score using the strategy: {total_score_1}")
            print(f"Solution 2: Total score using the new strategy: {total_score_2}")

    def get_solution_1(self, input_path):
        score_per_match = self.get_scores_per_match(input_path)
        total_score = sum(score_per_match)
        return total_score

    def get_solution_2(self, input_path):
        matches = read_lines_into_list(input_path)

        scores_per_match = []
        for match_list in matches:
            match_list = match_list.split(" ")
            opponent_play = ord(match_list[0].lower()) - 96
            needed_win_score = (ord(match_list[1].lower()) - 96 - 24)*3
            for my_play in [1, 2, 3]:
                possible_win_score = self.get_win_score(opponent_play, my_play)
                if possible_win_score == needed_win_score:
                    scores_per_match.append(my_play + needed_win_score)
        total_score = sum(scores_per_match)
        return total_score

    def get_scores_per_match(self, input_path):
        print(f"\nInput from: {input_path}")
        matches = read_lines_into_list(input_path)
        score_per_match = [self.get_score(match) for match in matches]
        return score_per_match

    def get_score(self, match):
        match_list = match.split(" ")
        opponent_play = ord(match_list[0].lower()) - 96
        my_play = ord(match_list[1].lower()) - 96 - 23
        win_score = self.get_win_score(
            opponent_play=opponent_play,
            my_play=my_play
        )
        return my_play + win_score

    def get_win_score(self, opponent_play, my_play):
        if my_play % 3 > opponent_play:
            win_score = 6
        elif my_play == opponent_play:
            win_score = 3
        else:
            win_score = 0
        if opponent_play == 2 and my_play == 3:
            win_score = 6
        if opponent_play == 3 and my_play == 1:
            win_score = 6
        return win_score


if __name__ == '__main__':
    day2_obj = Day2()
    day2_obj.main()
