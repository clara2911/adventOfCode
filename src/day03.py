from utils import read_lines_of_strings_into_list_of_chars


class Day3:

    def __init__(self):
        pass

    def main(self):
        test_input_path = '../inputs/day03/input_test.txt'
        final_input_path = '../inputs/day03/input.txt'
        for input_path in [test_input_path, final_input_path]:
            print(f"\nInput from: {input_path}")
            bag_contents = read_lines_of_strings_into_list_of_chars(input_path)
            sum_priorities_1 = self.get_solution_1(bag_contents=bag_contents)
            sum_priorities_2 = self.get_solution_2(bag_contents=bag_contents)
            print(f"Solution 1: {sum_priorities_1}")
            print(f"Solution 2: {sum_priorities_2}")

    def get_solution_1(self, bag_contents):
        priorities = []
        for bag_content in bag_contents:
            split = int(0.5*len(bag_content))
            first_compartment = bag_content[:split]
            second_compartment = bag_content[split:]
            overlapping_item = list(set([value for value in first_compartment if value in second_compartment]))
            assert len(overlapping_item) == 1
            priority = self.get_priority(overlapping_item)
            priorities.append(priority)
        return sum(priorities)

    def get_solution_2(self, bag_contents):
        num_groups = int(len(bag_contents) / 3)
        priorities = []
        for i in range(num_groups):
            group_bags = bag_contents[3*i:3*i+3]
            overlapping_item = list(set([
                item for item in group_bags[0] if item in group_bags[1] and item in group_bags[2]
            ]))
            assert len(overlapping_item) == 1
            priority = self.get_priority(overlapping_item)
            priorities.append(priority)
        return sum(priorities)

    def get_priority(self, item):
        priority = ord(item[0]) - ord('a') + 1
        if priority < 0:  # capital letter
            priority = priority + 2 * 26 + 6
        return priority


if __name__ == '__main__':
    day3_obj = Day3()
    day3_obj.main()
