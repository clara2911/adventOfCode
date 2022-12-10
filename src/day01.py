from utils import read_lines_into_list


class Day1:

    @staticmethod
    def main():
        test_input_path = '../inputs/day01/input_test.txt'
        final_input_path = '../inputs/day01/input.txt'
        for input_path in [test_input_path, final_input_path]:
            solution1, solution2 = Day1.get_solution(input_path=input_path)
            print(f"Solution 1: Max calories carried by one single elf: {solution1}")
            print(f"Solution 2: Total calories of the 3 elves with the most calories: {solution2}")

    @staticmethod
    def get_solution(input_path):
        print(f"\nInput from: {input_path}")
        calories_all_elves = read_lines_into_list(input_path)

        totals = []
        elf = 0
        for line in calories_all_elves:
            if line != '':
                elf += int(line)
            else:
                totals.append(elf)
                elf = 0
        totals.append(elf)

        totals.sort()
        max_calories = totals[-1]
        sum_of_3_max_calories = sum(totals[-3:])
        return max_calories, sum_of_3_max_calories


if __name__ == '__main__':
    Day1.main()
