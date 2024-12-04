from pathlib import Path
import logging
import day04
import re
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_part1_example_xmascount_matches_puzzle_description():
    xmas_count = day04.get_solution_part1(input_path=Path("../input/day04/test_input.txt"))
    assert xmas_count == 18


def test_part2_example_mascrossescount_matches_puzzle_description():
    mascrosses_count = day04.get_solution_part2(input_path=Path("../input/day04/test_input.txt"))
    assert mascrosses_count == 9


def test_horizontal_occurrences():
    crossword = day04.read_input(Path("../input/day04/test_input.txt"))
    n_lr = day04.n_occurrences(crossword)
    n_rl = day04.n_occurrences(crossword[:, ::-1])
    assert n_lr == 3
    assert n_rl == 2


def test_vertical_occurrences():
    crossword = day04.read_input(Path("../input/day04/test_input.txt"))
    n_up_down = day04.n_occurrences(np.rot90(crossword))
    n_down_up = day04.n_occurrences(np.rot90(crossword[::-1, :]))
    assert n_up_down == 1
    assert n_down_up == 2


def test_diagonal_occurrences():
    crossword = day04.read_input(Path("../input/day04/test_input.txt"))
    diagonals = day04.diagonal(crossword)
    n_diag_left_right = day04.n_occurrences(diagonals)
    diagonals_backwards = day04.diagonal(crossword[::-1, :])
    n_diag_right_left = day04.n_occurrences(diagonals_backwards)
    assert n_diag_left_right == 1
    assert n_diag_right_left == 4


def test_diagonal_occurrences_backwards():
    crossword = day04.read_input(Path("../input/day04/test_input.txt"))
    diagonals_backwards = day04.diagonal(crossword[::-1, :])
    n_diag_right_left = day04.n_occurrences(diagonals_backwards)
    assert n_diag_right_left == 4


# def test_all_diagonals():
#     crossword = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     all_diagonals = day04.all_diagonals(crossword)
#     expected_output = [np.array(x) for x in [[7], [4, 8], [1, 5, 9], [2, 6], [3]]]
#     assert [x == y for x, y in zip(all_diagonals, expected_output)] == [True]*5


def test_regex_returns_occurrences_of_xmas():
    text = "XMASBLABLABLAXAMSBLASAMXXMAS"
    pattern = "XMAS"
    matches = re.findall(pattern, text)
    assert len(matches) == 2
    assert matches == ["XMAS", "XMAS"]


def test_which_diagonal_is_which():
    crossword = day04.read_input(Path("../input/day04/test_input.txt"))
    diagonals = [
        day04.diagonal(crossword),
        day04.diagonal(crossword[:, ::-1]),
        day04.diagonal(crossword[::-1, ::-1]),
        day04.diagonal(crossword[::-1, :]),


    ]
    assert (diagonals[0][2] == np.array(['S', 'A', 'M'])).all()  # \ up down, so starting left bottom
    assert (diagonals[1][3] == np.array(['S', 'A', 'M', 'M'])).all()  # / up down, so starting right bottom
    assert (diagonals[2][3] == np.array(['X', 'M', 'M', 'M'])).all()  # \ down up, so starting left top
    assert (diagonals[3][2] == np.array(['A', 'S', 'M'])).all()  # / down up, so starting left top



