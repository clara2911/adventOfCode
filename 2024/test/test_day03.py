import unittest
from pathlib import Path
import logging
import day03
import re


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestDay03(unittest.TestCase):

	def test_part1_example_sum_of_multiplications_matches_puzzle_description(self):
		sum_multiplications = day03.get_solution_part1(input_path=Path("../input/day03/test_input_part1.txt"))
		self.assertEqual(sum_multiplications, 161)

	def test_part2_example_sum_of_multiplications_matches_puzzle_description(self):
		sum_multiplications = day03.get_solution_part2(input_path=Path("../input/day03/test_input_part2.txt"))
		self.assertEqual(sum_multiplications, 48)

	def test_regex_first_number(self):
		text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
		pattern = r"mul\((\d+),\d+\)"
		matches = re.findall(pattern, text)
		assert len(matches) == 4
		assert matches == ["2", "5", "11", "8"]

	def test_regex_second_number(self):
		text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
		pattern = r"mul\(\d+,(\d+)\)"
		matches = re.findall(pattern, text)
		assert len(matches) == 4
		assert matches == ["4", "5", "8", "5"]

	def test_regex_second_number_and_do_or_dont(self):
		text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
		pattern = r"(do\(\)|don't\(\)|mul\(\d+,(\d+)\))"
		matches = re.findall(pattern, text)
		matches = [submatch if submatch.isnumeric() else match for (match, submatch) in matches]
		assert len(matches) == 6
		assert matches == ["4", "don't()", "5", "8", "do()", "5"]


if __name__ == '__main__':
	unittest.main()
