from pathlib import Path
from day06 import day06_main


def test_part1_example_n_distinct_visited_positions_matches_puzzle_description():
    n_positions = day06_main.get_solution_part1(input_path=Path("../input/day06/test_input.txt"))
    assert n_positions == 41


def test_part2_example_n_obstacle_locations_matches_puzzle_description():
    n_obstacle_locations = day06_main.get_solution_part2(input_path=Path("../input/day06/test_input.txt"))
    assert n_obstacle_locations == 6


def test_read_input():
    map = day06_main.read_input(input_path=Path("../input/day06/test_input.txt"))
    assert map.shape == (10, 10)
    assert map[6, 4] == '^'


def test_read_input_letters():
    map = day06_main.read_input(input_path=Path("../input/day06/selfmade_test_input.txt"))
    assert map.shape == (2, 4)
    assert map[0, 0] == 'A'
    assert map[1, 3] == 'H'


def test_read_input_hashtags_not_comments():
    map = day06_main.read_input(input_path=Path("../input/day06/selfmade_test_input2.txt"))
    assert map.shape == (2, 4)
    assert map[0, 0] == '.'
    assert map[1, 3] == '#'



