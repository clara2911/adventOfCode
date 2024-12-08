from pathlib import Path
import numpy as np
import day08


def test_part1_example_n_antinodes_matches_puzzle_description():
    n_antinodes = day08.get_solution_part1(input_path=Path("../input/day08/test_input.txt"))
    assert n_antinodes == 14


def test_part1_example_n_antinodes_matches_tiny_example():
    n_antinodes = day08.get_solution_part1(input_path=Path("../input/day08/test_input_tiny.txt"))
    assert n_antinodes == 2


def test_part2_example_n_antinodes_matches_puzzle_description():
    n_antinodes = day08.get_solution_part2(input_path=Path("../input/day08/test_input.txt"))
    assert n_antinodes == 34


def test_read_input():
    roofs = day08.read_input(input_path=Path("../input/day08/test_input_tiny.txt"))
    assert roofs.shape == (4, 4)
    expected_output = np.array([
        ['.', '.', '.', '.'],
        ['.', 'a', '.', '.'],
        ['.', '.', 'a', '.'],
        ['.', '.', '.', '.']
    ])
    assert np.array_equal(roofs, expected_output)


def test_get_all_antinodes_for_frequency():
    roofs = np.array([
        ['.', '.', '.', '.'],
        ['.', 'a', '.', '.'],
        ['.', '.', 'a', '.'],
        ['.', '.', '.', '.']
    ])
    antinodes = day08.get_all_antinodes_for_frequency(roofs=roofs, frequency='a', min_harmonics=0, max_harmonics=1)
    assert antinodes == {(0, 0), (3, 3)}


def test_get_valid_antinodes():
    antinodes = day08.get_valid_antinodes(x_pair=(1, 2), y_pair=(1, 2), roof_shape=(4, 4), min_harmonics=0, max_harmonics=1)
    assert antinodes == {(0, 0), (3, 3)}


def test_get_valid_antinodes_with_possible_harmonics():
    antinodes = day08.get_valid_antinodes(x_pair=(1, 2), y_pair=(1, 2), roof_shape=(5, 5), min_harmonics=-1, max_harmonics=50)
    assert antinodes == {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)}
