import numpy as np
from day06.domain.state import Position


class MapReader:
	def __init__(self, map: np.ndarray):
		self.map=map
		self.walkable_locations: list[Position] = [Position(x, y) for x, y in zip(*np.where(map == '.'))]
		self.obstacle_locations: list[Position] = [Position(x, y) for x, y in zip(*np.where(map == '#'))]

	def is_obstacle_location(self, position: Position) -> bool:
		return position in self.obstacle_locations

	def get_walkable_locations(self) -> list[Position]:
		return self.walkable_locations

	def is_out_of_maze(self, position: Position) -> bool:
		return position.row < 0 or position.column < 0 or position.row >= self.map.shape[0] or position.column >= self.map.shape[1]

	def add_obstacle(self, position: Position):
		self.obstacle_locations.append(position)