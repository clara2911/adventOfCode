from utils import read_lines_into_list_of_lists
from day10_classes.cpu import CPU
from day10_classes.crt import CRT


class Day10:

    def __init__(self):
        test_input_path = '../inputs/day10/input_test.txt'
        final_input_path = '../inputs/day10/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]

        self.cycle_count = 0
        self.cpu = CPU()
        self.crt = CRT()

    def main(self):
        for input_path in self.all_input_paths:
            self.cycle_count = 0
            self.cpu = CPU()
            self.crt = CRT()
            print(f"\nInput from: {input_path}")
            instructions = self.parse_input(input_path)
            sum_signals = self.part1(instructions)
            crt_output = self.part2(instructions)
            print(f"Solution 1: {sum_signals}")
            print(f"Solution 2: {crt_output}")

    @staticmethod
    def parse_input(file_path):
        instructions = read_lines_into_list_of_lists(file_path, sep=" ")
        return instructions

    def part1(self, instructions):
        """ """
        for instruction in instructions:
            if instruction[0] == 'addx':
                self.do_addx(int(instruction[1]))
            if instruction[0] == 'noop':
                self.do_noop()
        return sum([(key+1)*value for key, value in self.cpu.signal_strengths.items()])

    def part2(self, instructions):
        """
        follow the instructions
        if the sprite at any moment in time is in the same place as the cursor of the crt
        then we draw a # otherwise the crt just draws a .

        """
        for instruction in instructions:
            if instruction[0] == 'addx':
                self.do_addx(int(instruction[1]))

            if instruction[0] == 'noop':
                self.do_noop()

        return "See print in terminal"

    def do_noop(self):
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)
        self.make_cycle()
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)
        self.cpu.noop()
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)

    def do_addx(self, number_to_add: int):
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)
        self.make_cycle()
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)
        self.make_cycle()
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)
        self.cpu.addx(v=number_to_add)
        self.cpu.check_signal_strenghts(cycle_count=self.cycle_count)

    def make_cycle(self):

        if self.overlap(self.cycle_count % 40, self.cpu.register):
            self.crt.draw_pixel(dark=True)
        else:
            self.crt.draw_pixel(dark=False)
        self.cycle_count += 1

    def overlap(self, x, y):
        return x == y or (x-1) == y or (x+1) == y


if __name__ == '__main__':
    day10 = Day10()
    day10.main()
