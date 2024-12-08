from pathlib import Path
import numpy as np


def get_solution_part1(input_path: Path) -> int:
	updates, rules = read_input(input_path)
	update_validity_mask = get_update_validity_mask(updates=updates, rules=rules)
	valid_updates = np.array(updates, dtype='object')[update_validity_mask]
	sum_middles = sum_middle_pagenumbers(updates=valid_updates)
	return sum_middles


def get_solution_part2(input_path: Path) -> int:
	updates, rules = read_input(input_path)
	update_validity_mask = get_update_validity_mask(updates=updates, rules=rules)
	invalid_updates = np.array(updates, dtype='object')[~update_validity_mask]
	reordered_updates = reorder_invalid_updates(invalid_updates=invalid_updates, rules=rules)
	sum_middles = sum_middle_pagenumbers(updates=reordered_updates)
	return sum_middles


def read_input(input_path: Path) -> tuple[list[list[int]], list[tuple[int, int]]]:
	with open(input_path) as f:
		content = f.read()
	rules_part, updates_part = content.split("\n\n")
	rules = [tuple(map(int, line.split('|'))) for line in rules_part.splitlines()]
	updates = [[int(num) for num in line.split(',')] for line in updates_part.splitlines()]
	return updates, rules


def get_update_validity_mask(updates: list[list[int]], rules: list[tuple[int, int]]) -> np.array:
	is_correctly_ordered = np.array([False] * len(updates))
	for i, update in enumerate(updates):
		is_correctly_ordered[i] = is_update_valid(update=update, rules=rules)
	return is_correctly_ordered


def is_update_valid(update: list[int], rules: list[tuple[int, int]]):
	for page_number in update:
		if not page_adheres_to_rules(page_number=page_number, update=update, rules=rules):
			break
		elif update.index(page_number) == len(update) - 1:
			return True
	return False


def find_rules_containing_page(rules: list[tuple[int, int]], page_number: int):
	return [rule for rule in rules if page_number in rule]


def page_adheres_to_rules(page_number: int, update: list[int], rules: list[tuple[int, int]]) -> bool:
	relevant_rules = find_rules_containing_page(rules=rules, page_number=page_number)
	for rule in relevant_rules:
		if rule[0] in update and rule[1] in update:
			if not update.index(rule[0]) < update.index(rule[1]):
				return False
	return True


def sum_middle_pagenumbers(updates: list[list[int]]) -> int:
	middle_pagenumbers = []
	for update in updates:
		middle_index = int((len(update)-1) / 2)
		middle_pagenumbers.append(update[middle_index])
	return sum(middle_pagenumbers)


def reorder_invalid_updates(invalid_updates: list[list[int]], rules: list[tuple[int, int]]) -> list[list[int]]:
	reordered_updates = []
	for i, update in enumerate(invalid_updates):
		while not is_update_valid(update=update, rules=rules):
			for page_number in update:
				if not page_adheres_to_rules(page_number=page_number, update=update, rules=rules):
					update = make_page_adhere_to_rules(page_number=page_number, update=update, rules=rules)
		reordered_updates.append(update)
	return reordered_updates


def make_page_adhere_to_rules(page_number: int, update: list[int], rules: list[tuple[int, int]]) -> list[int]:
	relevant_rules = find_rules_containing_page(rules=rules, page_number=page_number)
	while not page_adheres_to_rules(page_number=page_number, update=update, rules=rules):
		for rule in relevant_rules:
			if rule[0] in update and rule[1] in update:
				index0, index1 = update.index(rule[0]), update.index(rule[1])
				page0, page1 = update[index0], update[index1]
				if not index0 < index1:
					update[index0] = page1
					update[index1] = page0
	return update


if __name__ == '__main__':
	sum_middles = get_solution_part1(input_path=Path("../input/day05/input_day05.txt"))
	print(f"SOLUTION PART 1 // Sum of middle page numbers: {sum_middles}")
	sum_middles = get_solution_part2(input_path=Path("../input/day05/input_day05.txt"))
	print(f"SOLUTION PART 2 // Sum of middle page numbers of reordered invalid updates: {sum_middles}")
