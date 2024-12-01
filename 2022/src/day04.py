from utils import read_lines_into_list_of_lists


class Day4:

    def __init__(self):
        pass

    def main(self):
        test_input_path = '../inputs/day04/input_test.txt'
        final_input_path = '../inputs/day04/input.txt'
        for input_path in [test_input_path, final_input_path]:
            print(f"\nInput from: {input_path}")
            lines = read_lines_into_list_of_lists(file_path=input_path, sep=',')
            cleaning_pairs = [[elf.split('-') for elf in line] for line in lines]
            cleaning_pairs = [[[int(range_lim) for range_lim in elf] for elf in line] for line in cleaning_pairs]
            num_containing_pairs = self.part1(cleaning_pairs)
            num_overlapping_pairs = self.part2(cleaning_pairs)
            print(f"Solution 1: {num_containing_pairs}")
            print(f"Solution 2: {num_overlapping_pairs}")

    def part1(self, cleaning_pairs):
        num_containing_pairs = 0
        for cleaning_pair in cleaning_pairs:
            assert len(cleaning_pair) == 2
            task1 = cleaning_pair[0]
            task2 = cleaning_pair[1]
            assert len(task1) == 2 and len(task2) == 2
            if (
                    (int(task1[0]) <= int(task2[0])) and (int(task1[1]) >= int(task2[1]))
            ) or (
                    (int(task1[0]) >= int(task2[0])) and (int(task1[1]) <= int(task2[1]))
            ):
                num_containing_pairs += 1

        return num_containing_pairs

    def part2(self, cleaning_pairs):
        num_overlapping_pairs = 0
        for cleaning_pair in cleaning_pairs:
            assert len(cleaning_pair) == 2
            task1 = cleaning_pair[0]
            task2 = cleaning_pair[1]
            assert len(task1) == 2 and len(task2) == 2
            if (
                    (int(task1[0]) <= int(task2[1])) and (int(task1[1]) >= int(task2[0]))
            ) or (
                    (int(task2[0]) >= int(task1[1])) and (int(task2[1]) <= int(task1[0]))
            ):
                num_overlapping_pairs += 1

        return num_overlapping_pairs


if __name__ == '__main__':
    day4_obj = Day4()
    day4_obj.main()
