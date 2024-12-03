import re
from pathlib import Path


def get_solution_part1(input_path: Path) -> int:
	mul_instructions = read_input(input_path)
	first_numbers, second_numbers = extract_numbers_to_be_multiplied(mul_instructions)
	sum_multiplications = get_sum_multiplications(first_numbers=first_numbers, second_numbers=second_numbers)
	return sum_multiplications


def get_solution_part2(input_path: Path) -> int:
	mul_instructions = read_input(input_path)
	first_numbers, second_numbers = extract_numbers_to_be_multiplied_with_dos_and_donts(mul_instructions=mul_instructions)
	sum_multiplications = get_sum_multiplications(first_numbers=first_numbers, second_numbers=second_numbers)
	return sum_multiplications


def read_input(input_path: Path) -> str:
	multiplication_instructions = input_path.read_text()
	return multiplication_instructions


def extract_numbers_to_be_multiplied(mul_instructions: str) -> tuple[list[int], list[int]]:
	pattern_first_number = r"mul\((\d+),\d+\)"
	pattern_second_number = r"mul\(\d+,(\d+)\)"
	first_numbers = [int(number) for number in re.findall(pattern_first_number, mul_instructions)]
	second_numbers = [int(number) for number in re.findall(pattern_second_number, mul_instructions)]
	return first_numbers, second_numbers


def extract_numbers_to_be_multiplied_with_dos_and_donts(mul_instructions: str) -> tuple[list[int], list[int]]:
	pattern_first_number = r"(do\(\)|don't\(\)|mul\((\d+),\d+\))"
	pattern_second_number = r"(do\(\)|don't\(\)|mul\(\d+,(\d+)\))"
	matches_first_number = re.findall(pattern_first_number, mul_instructions)
	matches_second_number = re.findall(pattern_second_number, mul_instructions)
	matches_first_number = [int(submatch) if submatch.isnumeric() else match for (match, submatch) in matches_first_number]
	matches_second_number = [int(submatch) if submatch.isnumeric() else match for (match, submatch) in matches_second_number]

	do_state = True
	new_first_numbers = []
	new_second_numbers = []
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




def get_sum_multiplications(first_numbers: list[int], second_numbers: list[int]) -> int:
	multiplications = [first * second for first, second in zip(first_numbers, second_numbers)]
	sum_multiplications = sum(multiplications)
	return sum_multiplications


if __name__ == '__main__':
	sum_multiplications = get_solution_part1(input_path=Path("../input/day03/input_day03.txt"))
	print(f"SOLUTION PART 1 // Sum of multiplications: {sum_multiplications}")
	sum_multiplications = get_solution_part2(input_path=Path("../input/day03/input_day03.txt"))
	print(f"SOLUTION PART 2 // Sum multiplications with dos() and don'ts(): {sum_multiplications}")



