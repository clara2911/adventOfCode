import unittest
from pathlib import Path
import logging
import day01


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestDay01(unittest.TestCase):

	def test_example_distance_sum_matches_puzzle_description(self):
		distance_sum = day01.get_solution_part1(input_path=Path("../input/day01/test_input_part1.txt"))
		self.assertEqual(distance_sum, 11)

	def test_example_similarity_score_matches_puzzle_description(self):
		similarity_score = day01.get_solution_part2(input_path=Path("../input/day01/test_input_part2.txt"))
		self.assertEqual(similarity_score, 31)


if __name__ == '__main__':
	unittest.main()
