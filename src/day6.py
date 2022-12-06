from utils import read_lines_into_list


class Day6:

    def __init__(self):
        self.test_input_path = '../inputs/day6/input_test.txt'
        self.final_input_path = '../inputs/day6/input.txt'
        self.all_input_paths = [self.test_input_path, self.final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            datastream = self.parse_input(input_path)
            n_processed_chars_before_packet_start = self.part1(datastream=datastream)
            n_processed_chars_before_message = self.part2(datastream=datastream)
            print(f"Solution 1: {n_processed_chars_before_packet_start}")
            print(f"Solution 2: {n_processed_chars_before_message}")

    def parse_input(self, input_path):
        datastream_lines = read_lines_into_list(input_path)
        assert len(datastream_lines) == 1  # only 1 line
        return [*datastream_lines[0]]

    def part1(self, datastream: list):
        char1, char2, char3 = datastream[0], datastream[1], datastream[2]
        # print(f"{char1}, {char2}, {char3}")
        for i, next_char in enumerate(datastream[3:]):
            # print(i)
            # print(f"{char1}, {char2}, {char3}, {next_char}")
            if len(set([char1, char2, char3, next_char])) == 4:
                num_processed_chars = i + 4
                return num_processed_chars
            else:
                char1 = char2
                char2 = char3
                char3 = next_char
        return 9999999  # something went wrong

    def part2(self, datastream: list):
        prev_chars = [datastream[i] for i in range(13)]
        # print(f"{char1}, {char2}, {char3}")
        for i, next_char in enumerate(datastream[13:]):
            # print(i)
            # print(f"{char1}, {char2}, {char3}, {next_char}")
            if len(set(prev_chars + [next_char])) == 14:
                num_processed_chars = i + 14
                return num_processed_chars
            else:
                prev_chars = prev_chars[1:] + [next_char]
        return 9999999  # something went wrong


if __name__ == '__main__':
    day6_obj = Day6()
    day6_obj.main()
