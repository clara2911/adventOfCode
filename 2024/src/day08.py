import itertools
from pathlib import Path
import numpy as np


def get_solution_part1(input_path: Path) -> int:
	roofs = read_input(input_path)
	antenna_frequencies = np.unique(roofs.flatten())
	antenna_frequencies = antenna_frequencies[antenna_frequencies != '.']
	antinodes = set()
	for frequency in antenna_frequencies:
		antinodes.update(get_all_antinodes_for_frequency(roofs=roofs, frequency=frequency, min_harmonics=0, max_harmonics=1))
	return len(antinodes)


def get_solution_part2(input_path: Path) -> int:
	roofs = read_input(input_path)
	antenna_frequencies = np.unique(roofs.flatten())
	antenna_frequencies = antenna_frequencies[antenna_frequencies != '.']
	antinodes = set()
	for frequency in antenna_frequencies:
		antinodes.update(get_all_antinodes_for_frequency(roofs=roofs, frequency=frequency, min_harmonics=-1, max_harmonics=50))
	return len(antinodes)


def read_input(input_path: Path) -> np.ndarray:
	roofs = np.loadtxt(input_path, dtype=str, comments=None)
	roofs = np.array([list(row) for row in roofs])
	return roofs


def get_all_antinodes_for_frequency(roofs: np.ndarray, frequency: np.array, min_harmonics: int, max_harmonics: int) -> set:
	antinodes = set()
	indices = np.where(roofs == frequency)
	x_indices, y_indices = indices[0], indices[1]
	x_antenna_pairs = np.array(list(itertools.combinations(x_indices, 2)))
	y_antenna_pairs = np.array(list(itertools.combinations(y_indices, 2)))
	for x_pair, y_pair in zip(x_antenna_pairs, y_antenna_pairs):
		valids = get_valid_antinodes(x_pair=x_pair, y_pair=y_pair, roof_shape=roofs.shape, min_harmonics=min_harmonics, max_harmonics=max_harmonics)
		antinodes.update(valids)
	return antinodes


def get_valid_antinodes(x_pair: tuple[int, int], y_pair: tuple[int, int], roof_shape: tuple[int, int], min_harmonics=-1, max_harmonics: int=50) -> set:
	antinodes = set()
	delta_x = x_pair[1] - x_pair[0]
	delta_y = y_pair[1] - y_pair[0]
	possible_antinodes = set()
	for i in range(min_harmonics, max_harmonics):
		antinode_minus = (x_pair[0] - (i+1)*delta_x, y_pair[0] - (i+1)*delta_y)
		antinode_plus = (x_pair[1] + (i+1)*delta_x, y_pair[1] + (i+1)*delta_y)
		possible_antinodes.add(antinode_minus)
		possible_antinodes.add(antinode_plus)
	for possible_antinode in possible_antinodes:
		if (0 <= possible_antinode[0] < roof_shape[0]) and (0 <= possible_antinode[1] < roof_shape[1]):
			antinodes.add(possible_antinode)
	return antinodes


if __name__ == '__main__':
	n_antinodes = get_solution_part1(input_path=Path("../input/day08/input_day08.txt"))
	print(f"SOLUTION PART 1 // N antinodes: {n_antinodes}")
	n_resonant_antinodes = get_solution_part2(input_path=Path("../input/day08/input_day08.txt"))
	print(f"SOLUTION PART 2 // N antinodes: {n_resonant_antinodes}")
