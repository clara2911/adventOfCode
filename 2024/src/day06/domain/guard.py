from collections import defaultdict
from day06.domain.state import Position, Direction


class Guard:
	def __init__(self, start_position: Position, start_direction: Direction):
		self.current_position: Position = start_position
		self.direction: Direction = start_direction
		self.visited_positions: list[Position] = [self.current_position]
		self.faced_directions: defaultdict[Position, list[Direction]] = defaultdict(list)
		self.faced_directions[self.current_position] = [self.direction]

	def get_next_position(self):
		match self.direction:
			case Direction.NORTH:
				next_position = Position(row=self.current_position.row - 1, column=self.current_position.column)
			case Direction.EAST:
				next_position = Position(row=self.current_position.row, column=self.current_position.column + 1)
			case Direction.SOUTH:
				next_position = Position(row=self.current_position.row + 1, column=self.current_position.column)
			case Direction.WEST:
				next_position = Position(row=self.current_position.row, column=self.current_position.column - 1)
		return next_position

	def step_forward(self):
		next_position = self.get_next_position()
		self.current_position = next_position
		self.visited_positions.append(next_position)
		self.faced_directions[self.current_position].append(self.direction)

	def remove_position_from_visited_list(self):
		self.visited_positions.remove(self.current_position)

	def turn_right(self):
		match self.direction:
			case Direction.NORTH:
				self.direction = Direction.EAST
			case Direction.EAST:
				self.direction = Direction.SOUTH
			case Direction.SOUTH:
				self.direction = Direction.WEST
			case Direction.WEST:
				self.direction = Direction.NORTH
		self.faced_directions[self.current_position].append(self.direction)

	def is_in_loop(self):
		return len(self.faced_directions[self.current_position]) > len(set(self.faced_directions[self.current_position]))

	def get_n_visited_positions(self):
		unique_positions = {}
		for position in self.visited_positions:
			unique_positions[position] = None
		return len(unique_positions)
