from pathlib import Path
import pandas as pd


def get_solution_part1(input_path: Path) -> int:
	coordinates = read_input(input_path)
	return distance_sum(coordinates)


def get_solution_part2(input_path: Path) -> int:
	coordinates = read_input(input_path)
	return similarity_score(coordinates)


def read_input(input_path: Path) -> pd.DataFrame:
	coordinates = pd.read_csv(
		input_path,
		sep="   ",
		header=None,
		names=["search_group1", "search_group2"],
		dtype={"search_group1": int, "search_group2": int},
		engine='python'
	)
	return coordinates


def similarity_score(coordinates: pd.DataFrame) -> int:
	value_counts = coordinates['search_group2'].value_counts().to_dict()
	n_occurrences = [value_counts.get(coord, 0) for coord in coordinates['search_group1']]
	similarities = coordinates['search_group1'] * n_occurrences
	return similarities.sum()


def distance_sum(coordinates: pd.DataFrame) -> int:
	coordinates['search_group1'] = coordinates['search_group1'].sort_values().reset_index(drop=True)
	coordinates['search_group2'] = coordinates['search_group2'].sort_values().reset_index(drop=True)
	coordinates['difference'] = abs(coordinates['search_group2'] - coordinates['search_group1'])
	return coordinates['difference'].sum()


if __name__ == '__main__':
	distance_sum = get_solution_part1(input_path=Path("../input/day01/input_day01.txt"))
	print(f"SOLUTION PART 1 // Distance sum: {distance_sum}")

	similarity_score = get_solution_part2(input_path=Path("../input/day01/input_day01.txt"))
	print(f"SOLUTION PART 2 // similarity score: {similarity_score}")

