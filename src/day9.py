from utils import read_lines_into_list_of_lists


class Day9:

    def __init__(self):
        test_input_path = '../inputs/day9/input_test.txt'
        final_input_path = '../inputs/day9/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            head_movement = self.parse_input(input_path)
            num_visited_positions1 = self.part1(head_movement)
            num_visited_positions2 = self.part2(head_movement)
            print(f"Solution 1: {num_visited_positions1}")
            print(f"Solution 2: {num_visited_positions2}")

    def parse_input(self, file_path, sep=" "):
        with open(file_path) as f:
            list_of_lines = f.read().splitlines()
            head_movement = [line.split(sep) for line in list_of_lines]
        return head_movement

    def part1(self, head_movements):
        """
        keep the position of the head
        keep the position of the tail
        tail should follow head either horizontally, vertically or diagonally
        """
        head_pos = Position(start_position=[0, 0])
        tail_pos = Position(start_position=[0, 0])
        for move in head_movements:
            direction = move[0]
            num_iterations = int(move[1])
            for i in range(num_iterations):
                head_pos.move(direction=direction)
                if self.gotta_follow(head_pos=head_pos, tail_pos=tail_pos):
                    self.follow(head_pos=head_pos, tail_pos=tail_pos)
        num_positions_in_history = self.get_num_positions_in_history(tail_pos)
        return num_positions_in_history

    def part2(self, head_movements):
        """
        keep the position of the head
        keep the position of the tail
        tail should follow head either horizontally, vertically or diagonally
        """
        head_pos = Position(start_position=[0, 0])
        following_positions = [Position(start_position=[0, 0]) for _ in range(9)]
        for move in head_movements:
            direction = move[0]
            num_iterations = int(move[1])
            for i in range(num_iterations):
                head_pos.move(direction=direction)

                pos_to_follow = head_pos
                for following_pos in following_positions:
                    if self.gotta_follow(head_pos=pos_to_follow, tail_pos=following_pos):
                        self.follow(head_pos=pos_to_follow, tail_pos=following_pos)
                    pos_to_follow = following_pos

        num_positions_in_history = self.get_num_positions_in_history(following_positions[-1])
        return num_positions_in_history

    def gotta_follow(self, head_pos, tail_pos):
        reason1 = abs(head_pos.position[0] - tail_pos.position[0]) > 1
        reason2 = abs(head_pos.position[1] - tail_pos.position[1]) > 1
        return reason1 or reason2

    def follow(self, head_pos, tail_pos):
        if self.same_row(head_pos, tail_pos):
            if tail_pos.position[1] - head_pos.position[1] > 1:
                tail_pos.move('L')
            elif tail_pos.position[1] - head_pos.position[1] < -1:
                tail_pos.move('R')
        elif self.same_column(head_pos, tail_pos):
            if tail_pos.position[0] - head_pos.position[0] > 1:
                tail_pos.move('U')
            elif tail_pos.position[0] - head_pos.position[0] < -1:
                tail_pos.move('D')
        else:  # follow diagonally
            # first part of the move
            if tail_pos.position[0] - head_pos.position[0] > 0:
                tail_pos.move('U', add_to_position_history=False)
            else:
                tail_pos.move('D', add_to_position_history=False)
            # second part of the move
            if tail_pos.position[1] - head_pos.position[1] > 0:
                tail_pos.move('L')
            else:
                tail_pos.move('R')

    def same_row(self, pos1, pos2):
        return pos2.position[0] == pos1.position[0]

    def same_column(self, pos1, pos2):
        return pos2.position[1] == pos1.position[1]

    def get_num_positions_in_history(self, pos):
        pos_history = []
        for elem in pos.position_history:
            if elem not in pos_history:
                pos_history.append(elem)
        return len(pos_history)


class Position:
    def __init__(self, start_position):
        self.position = start_position
        self.position_history = [start_position.copy()]

    def move(self, direction, add_to_position_history=True):
        if direction == 'U':
            self.position[0] -= 1
        elif direction == 'D':
            self.position[0] += 1
        elif direction == 'L':
            self.position[1] -= 1
        elif direction == 'R':
            self.position[1] += 1

        else:
            raise ValueError(f'direction {direction} is not a valid input')
        if add_to_position_history:
            self.position_history.append(self.position.copy())


if __name__ == '__main__':
    day9_obj = Day9()
    day9_obj.main()
