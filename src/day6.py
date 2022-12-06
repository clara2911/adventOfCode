from utils import read_lines_into_list


class Day6:

    def __init__(self):
        test_input_path = '../inputs/day6/input_test.txt'
        final_input_path = '../inputs/day6/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            datastream = self.parse_input(input_path)
            n_processed_chars_before_packet_start = self.get_char_count_before_n_different(
                datastream=datastream,
                n_different=4
            )
            n_processed_chars_before_message = self.get_char_count_before_n_different(
                datastream=datastream,
                n_different=14
            )
            print(f"Solution 1: {n_processed_chars_before_packet_start}")
            print(f"Solution 2: {n_processed_chars_before_message}")

    @staticmethod
    def parse_input(input_path):
        datastream_lines = read_lines_into_list(input_path)
        assert len(datastream_lines) == 1  # only 1 line
        return [*datastream_lines[0]]

    def get_char_count_before_n_different(self, datastream: list, n_different):
        prev_chars = [datastream[i] for i in range(n_different-1)]
        for i, next_char in enumerate(datastream[n_different-1:]):
            if self.contains_no_duplicates(prev_chars + [next_char]):
                num_processed_chars = i + n_different
                return num_processed_chars
            else:
                prev_chars = prev_chars[1:] + [next_char]
        return 9999999  # something went wrong

    @staticmethod
    def contains_no_duplicates(element_list: list):
        return len(set(element_list)) == len(element_list)


if __name__ == '__main__':
    day6_obj = Day6()
    day6_obj.main()
