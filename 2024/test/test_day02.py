import unittest
from pathlib import Path
import logging
import day02
import numpy as np


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestDay02(unittest.TestCase):

	def test_part1_example_safety_count_matches_puzzle_description(self):
		safety_count = day02.get_solution_part1(input_path=Path("../input/day02/test_input.txt"))
		self.assertEqual(safety_count, 2)

	def test_read_input(self):
		research_data = day02.read_input(input_path=Path("../input/day02/test_input.txt"))
		assert len(research_data) == 6
		assert type(research_data[0]) == np.ndarray
		assert len(research_data[0]) == 5

	def test_part2_safety_count_with_problem_dampener_matches_puzzle_description(self):
		safety_count = day02.get_solution_part2(input_path=Path("../input/day02/test_input.txt"))
		assert safety_count == 4


if __name__ == '__main__':
	unittest.main()
