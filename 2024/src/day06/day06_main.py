from pathlib import Path
import numpy as np
from day06.domain.map_reader import MapReader
from day06.domain.guard import Guard
from day06.domain.state import Position, Direction


def get_solution_part1(input_path: Path) -> int:
	map_matrix = read_input(input_path=input_path)
	map_reader = MapReader(map=map_matrix)
	start_position = np.where(map_matrix == "^")
	guard = Guard(start_position=Position(row=start_position[0][0], column=start_position[1][0]), start_direction=Direction.NORTH)
	while not map_reader.is_out_of_maze(guard.current_position):
		if map_reader.is_obstacle_location(position=guard.get_next_position()):
			guard.turn_right()
		else:
			guard.step_forward()
	guard.remove_position_from_visited_list()  # last step was out of maze so remove
	return guard.get_n_visited_positions()


def get_solution_part2(input_path: Path) -> int:
	map_matrix = read_input(input_path=input_path)
	map_reader = MapReader(map=map_matrix)
	start_position = np.where(map_matrix == "^")
	loopy_obstacle_positions = []
	for obstacle_position in map_reader.get_walkable_locations():
		print(f"Obstacle position: {obstacle_position}")
		map_reader = MapReader(map=map_matrix)
		map_reader.add_obstacle(obstacle_position)
		if is_loop_when_obstacle_placed(start_position=start_position, map_reader=map_reader, obstacle_position=obstacle_position):
			loopy_obstacle_positions.append(obstacle_position)
	return len(set(loopy_obstacle_positions))


def is_loop_when_obstacle_placed(start_position, map_reader, obstacle_position):
	guard = Guard(start_position=Position(row=start_position[0][0], column=start_position[1][0]), start_direction=Direction.NORTH)
	while not map_reader.is_out_of_maze(guard.current_position):
		if map_reader.is_obstacle_location(position=guard.get_next_position()):
			guard.turn_right()
		else:
			guard.step_forward()
		if guard.is_in_loop():
			print(f"Loop detected at {obstacle_position}")
			return True
	return False


def read_input(input_path: Path) -> np.ndarray:
	map = np.loadtxt(input_path, dtype=str, comments=None)
	map = np.array([list(row) for row in map])
	return map


if __name__ == '__main__':
	n_positions = get_solution_part1(input_path=Path("../../input/day06/input_day06.txt"))
	print(f"SOLUTION PART 1 // N distinct visited positions: {n_positions}")
	n_obstacle_locations = get_solution_part2(input_path=Path("../../input/day06/input_day06.txt"))
	print(f"SOLUTION PART 2 // N loops: {n_obstacle_locations}")
