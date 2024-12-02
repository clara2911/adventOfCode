from pathlib import Path
import numpy as np


def get_solution_part1(input_path: Path) -> int:
	research_data = read_input(input_path)
	return safety_count(research_data=research_data)


def get_solution_part2(input_path: Path) -> int:
	research_data = read_input(input_path)
	return safety_count_with_problem_dampener(research_data=research_data)


def read_input(input_path: Path) -> list[np.ndarray]:
	with open(input_path) as f:
		research_data = [list(map(int, line.split())) for line in f]
	research_data = [np.array(row) for row in research_data]
	return research_data


def safety_count(research_data: list[np.ndarray]) -> int:
	safety_count = 0
	for levels_line in research_data:
		if is_safe(levels_line):
			safety_count += 1
	return safety_count


def safety_count_with_problem_dampener(research_data: list[np.ndarray]) -> int:
	safety_count = 0
	for levels_line in research_data:
		if is_safe(levels_line):
			safety_count += 1
		else:
			for i in range(len(levels_line)):
				levels_line_with_one_removed = np.delete(np.copy(levels_line), i)
				if is_safe(levels_line_with_one_removed):
					safety_count += 1
					break
	return safety_count


def is_safe(levels_line):
	differences = np.diff(levels_line)  # consecutive differences between levels
	return all_decreasing_or_increasing(differences, max_gap=3)


def all_decreasing_or_increasing(differences, max_gap):
	is_increasing_or_decreasing = (differences < 0).all() or (differences > 0).all()
	is_max_gap = (differences <= max_gap).all() and (differences >= -max_gap).all()
	return is_increasing_or_decreasing and is_max_gap


if __name__ == '__main__':
	safety_count = get_solution_part1(input_path=Path("../input/day02/input_day02.txt"))
	print(f"SOLUTION PART 1 // Safety count: {safety_count}")
	safety_count = get_solution_part2(input_path=Path("../input/day02/input_day02.txt"))
	print(f"SOLUTION PART 2 // Safety count: {safety_count}")



