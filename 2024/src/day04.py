import re
from pathlib import Path
import numpy as np


def get_solution_part1(input_path: Path) -> int:
	crossword = read_input(input_path)
	n_lr = n_occurrences(crossword)
	n_rl = n_occurrences(crossword[:, ::-1])
	n_du = n_occurrences(np.rot90(crossword))
	n_ud = n_occurrences(np.rot90(crossword[::-1, :]))
	n_diaglrud = n_occurrences(diagonal(crossword))
	n_diagrlud = n_occurrences(diagonal(crossword[::-1, :]))
	n_diaglrdu = n_occurrences(diagonal(crossword[:, ::-1]))
	n_diagrldu = n_occurrences(diagonal(crossword[::-1, ::-1]))
	n_xmas = n_lr + n_rl + n_du + n_ud + n_diaglrud + n_diagrlud + n_diaglrdu + n_diagrldu
	return n_xmas


def get_solution_part2(input_path: Path) -> int:
	crossword = read_input(input_path)
	n_mascross = sum([
		sum([
			int(is_mascross(crossword=crossword, i=i, j=j))
			if ((char == 'A') and (not side(j, crossword))) else 0
			for j, char in enumerate(row)
		])
		if not side(i, crossword) else 0
		for i, row in enumerate(crossword)
	])
	return n_mascross

def read_input(input_path):
	cw = np.loadtxt(input_path, delimiter=" ", dtype=str)
	cw = np.array([np.array([*row]) for row in cw])
	return cw


def n_occurrences(crossword: np.array) -> int:
	crossword = np.array([''.join(row) for row in crossword])
	crossword = '_'.join(crossword.flatten())
	xmas = re.findall("XMAS", crossword)
	n_xmas = len(xmas)
	return n_xmas


def diagonal(matrix1):
	rows, cols = matrix1.shape
	diagonals = [matrix1.diagonal(i) for i in range(-rows + 1, cols)]
	return diagonals


def side(i: int, ndarray: np.array):
	""" index is on the of the sides/edges of the ndarray"""
	return (i == 0) or (i == len(ndarray) - 1)


def is_mascross(crossword: np.array, i: int, j: int) -> bool:
	top_left = crossword[i - 1, j - 1]
	top_right = crossword[i - 1, j + 1]
	bottom_left = crossword[i + 1, j - 1]
	bottom_right = crossword[i + 1, j + 1]
	return (top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S') or \
	(top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M') or \
	(top_left == 'M' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'S') or \
	(top_left == 'S' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'M')



if __name__ == '__main__':
	n_xmas = get_solution_part1(input_path=Path("../input/day04/input_day04.txt"))
	print(f"SOLUTION PART 1 // Number of times XMAS occurs: {n_xmas}")
	n_mascross = get_solution_part2(input_path=Path("../input/day04/input_day04.txt"))
	print(f"SOLUTION PART 2 // Number of times a MAS-cross occurs: {n_mascross}")
