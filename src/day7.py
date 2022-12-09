from utils import read_lines_into_list
from typing import Dict


class Day7:

    def __init__(self):
        test_input_path = '../inputs/day7/input_test.txt'
        final_input_path = '../inputs/day7/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            dir_structure = self.parse_input(input_path)
            print(f"dir structure: {dir_structure}")
            total_dir_size = self.part1(dir_structure)
            size_of_dir_to_delete = self.part2(dir_structure)
            print(f"Solution 1: {total_dir_size}")
            print(f"Solution 2: {size_of_dir_to_delete}")

    def parse_input(self, file_path):
        list_of_lines = read_lines_into_list(file_path)
        dir_structure, i_inner, current_path = self.parse_lines(list_of_lines)
        return dir_structure

    def parse_lines(self, list_of_lines, current_path=""):
        dir_structure = {}
        i = 0
        current_path = current_path
        while i < len(list_of_lines):
            line = list_of_lines[i]
            # cd means start a new key / add a key
            if line == '$ cd ..':
                current_path = '+'.join(current_path.split("+")[:-1])
                return dir_structure, i, current_path
            elif line.startswith('$ cd'):

                dir_name = f"{current_path}+{line[5:]}"
                current_path = dir_name
                inner_dir_structure, i_inner, current_path = self.parse_lines(list_of_lines[i+1:], current_path)
                dir_structure[dir_name] = inner_dir_structure
                i += i_inner + 1
            elif line.startswith('$ ls'):
                # ls add all the next lines (until next command) to dictionary at this level
                pass
            elif line.startswith('dir'):
                pass  # don't need this if you never cd it
            else:  # 444 abc.txt means add {abc.text: 444}
                file_size, file_name = line.split(' ')
                dir_structure[file_name] = int(file_size)
            i += 1
        return dir_structure, i, current_path

    def part1(self, dir_structure):
        total_dir_size = self.get_total_dir_size_up_to_max_size(dir_structure, max_size=100000)
        return total_dir_size

    def part2(self,  dir_structure: Dict, needed_space=30000000):
        recursive_dir_sizes = self.get_recursive_dir_sizes_of_all_dirs(dir_structure)
        free_space = self.get_total_free_space(recursive_dir_sizes)
        space_to_free = needed_space - free_space
        sizes_above_min = {}
        for dir_name, dir_size in recursive_dir_sizes.items():
            if dir_size >= space_to_free:
                sizes_above_min[dir_name] = dir_size
        return min(sizes_above_min.values())

    def get_total_dir_size_up_to_max_size(self, dir_structure: Dict, max_size):
        sizes_below_max = {}
        recursive_dir_sizes = self.get_recursive_dir_sizes_of_all_dirs(dir_structure)
        for dir_name, dir_size in recursive_dir_sizes.items():
            if dir_size <= max_size:
                sizes_below_max[dir_name] = dir_size
        return sum(sizes_below_max.values())

    def get_total_free_space(self, recursive_dir_sizes, total_space=70000000):
        used_space = recursive_dir_sizes['+/']
        free_space = total_space - used_space
        return free_space

    def get_recursive_dir_sizes_of_all_dirs(self, dir_structure: dict):
        """
        Get recursive dir sizes per directory in nested_dir_structure
        :param dir_structure:
        :return: a flat dictionary with keys directory names and values recursive directory sizes
        """
        recursive_dir_sizes = {}
        for dir_or_file, content in dir_structure.items():
            assert type(content) == int or type(content) == dict
            if type(content) == int:  # it's a file
                pass
            elif type(content) == dict:  # it's a dir
                recursive_size = self.get_total_dir_size_of_topmost_dir(content)
                inner_dir_sizes = self.get_recursive_dir_sizes_of_all_dirs(content)
                recursive_dir_sizes.update(inner_dir_sizes)
                recursive_dir_sizes[dir_or_file] = recursive_size
        return recursive_dir_sizes

    def get_total_dir_size_of_topmost_dir(self, dir_structure: dict):
        """get total dir size for @param dir_structure"""
        total_dir_size = 0
        for file_or_dir_name, content in dir_structure.items():
            assert type(content) == int or type(content) == dict
            if type(content) == int:
                total_dir_size += content
            elif type(content) == dict:
                total_dir_size += self.get_total_dir_size_of_topmost_dir(content)
        return total_dir_size


if __name__ == '__main__':
    day7_obj = Day7()
    day7_obj.main()
