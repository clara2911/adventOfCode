import re
from pathlib import Path


def get_solution_part1(input_path: Path) -> int:
	mul_instructions = input_path.read_text()
	first_numbers, second_numbers = extract_numbers_to_be_multiplied(mul_instructions)
	return sum([first * second for first, second in zip(first_numbers, second_numbers)])


def get_solution_part2(input_path: Path) -> int:
	mul_instructions = input_path.read_text()
	first_numbers, second_numbers = extract_numbers_to_be_multiplied_with_commands(mul_instructions=mul_instructions)
	return sum([first * second for first, second in zip(first_numbers, second_numbers)])


def extract_numbers_to_be_multiplied(mul_instructions: str) -> tuple[list[int], list[int]]:
	pattern_first_number = r"mul\((\d+),\d+\)"
	pattern_second_number = r"mul\(\d+,(\d+)\)"
	first_numbers = [int(number) for number in re.findall(pattern_first_number, mul_instructions)]
	second_numbers = [int(number) for number in re.findall(pattern_second_number, mul_instructions)]
	return first_numbers, second_numbers


def extract_numbers_to_be_multiplied_with_commands(mul_instructions: str) -> tuple[list[int], list[int]]:
	matches_first_number = get_matches_with_commands(mul_instructions, pattern=r"(do\(\)|don't\(\)|mul\((\d+),\d+\))")
	matches_second_number = get_matches_with_commands(mul_instructions, pattern=r"(do\(\)|don't\(\)|mul\(\d+,(\d+)\))")

	do_state = True
	new_first_numbers, new_second_numbers = [], []
	for first_number, second_number in zip(matches_first_number, matches_second_number):
		if first_number == "don't()":
			do_state = False
		if first_number == "do()":
			do_state = True
			continue
		if do_state:
			new_first_numbers.append(first_number)
			new_second_numbers.append(second_number)
	return new_first_numbers, new_second_numbers


def get_matches_with_commands(mul_instructions: str, pattern: str) -> list[int]:
	matches_second_number = re.findall(pattern, mul_instructions)
	matches_second_number = [int(submatch) if submatch.isnumeric() else match for (match, submatch) in
							 matches_second_number]
	return matches_second_number


if __name__ == '__main__':
	sum_multiplications = get_solution_part1(input_path=Path("../input/day03/input_day03.txt"))
	print(f"SOLUTION PART 1 // Sum of multiplications: {sum_multiplications}")
	sum_multiplications = get_solution_part2(input_path=Path("../input/day03/input_day03.txt"))
	print(f"SOLUTION PART 2 // Sum multiplications with dos() and don'ts(): {sum_multiplications}")
