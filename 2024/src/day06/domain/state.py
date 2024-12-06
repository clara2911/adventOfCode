from dataclasses import dataclass
from enum import Enum


@dataclass
class Position:
	row: int
	column: int

	def __eq__(self, other):
		if isinstance(other, Position):
			return self.row == other.row and self.column == other.column
		return False

	def __hash__(self):
		return hash((self.row, self.column))


class Direction(Enum):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3
