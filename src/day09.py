
class Day9:

    def __init__(self):
        test_input_path = '../inputs/day09/input_test.txt'
        final_input_path = '../inputs/day09/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            head_movement = self.parse_input(input_path)
            num_visited_positions1 = self.part1(head_movement)
            num_visited_positions2 = self.part2(head_movement)
            print(f"Solution 1: {num_visited_positions1}")
            print(f"Solution 2: {num_visited_positions2}")

    @staticmethod
    def parse_input(file_path, sep=" "):
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
                if tail_pos.gotta_follow(pos_to_follow=head_pos):
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
                    if following_pos.gotta_follow(pos_to_follow=pos_to_follow):
                        self.follow(head_pos=pos_to_follow, tail_pos=following_pos)
                    pos_to_follow = following_pos

        num_positions_in_history = self.get_num_positions_in_history(following_positions[-1])
        return num_positions_in_history

    @staticmethod
    def follow(head_pos, tail_pos):
        if tail_pos.same_row(head_pos):
            if tail_pos.position[1] - head_pos.position[1] > 1:
                tail_pos.move('L')
            elif tail_pos.position[1] - head_pos.position[1] < -1:
                tail_pos.move('R')
        elif tail_pos.same_column(head_pos):
            if tail_pos.position[0] - head_pos.position[0] > 1:
                tail_pos.move('U')
            elif tail_pos.position[0] - head_pos.position[0] < -1:
                tail_pos.move('D')
        else:  # follow diagonally
            if tail_pos.position[0] - head_pos.position[0] > 0:
                tail_pos.move('U', add_to_position_history=False)
            else:
                tail_pos.move('D', add_to_position_history=False)
            if tail_pos.position[1] - head_pos.position[1] > 0:
                tail_pos.move('L')
            else:
                tail_pos.move('R')

    @staticmethod
    def get_num_positions_in_history(pos):
        distinct_positions = []
        distinct_positions = [
            distinct_positions.append(pos) for pos in pos.position_history if pos not in distinct_positions
        ]
        return len(distinct_positions)


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

    def gotta_follow(self, pos_to_follow):
        reason1 = abs(pos_to_follow.position[0] - self.position[0]) > 1
        reason2 = abs(pos_to_follow.position[1] - self.position[1]) > 1
        return reason1 or reason2

    def same_row(self, other_pos):
        return self.position[0] == other_pos.position[0]

    def same_column(self, other_pos):
        return self.position[1] == other_pos.position[1]


if __name__ == '__main__':
    day9_obj = Day9()
    day9_obj.main()
