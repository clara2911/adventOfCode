from utils import read_lines_into_matrix
from typing import Dict
import numpy as np


class Day8:

    def __init__(self):
        test_input_path = '../inputs/day8/input_test.txt'
        final_input_path = '../inputs/day8/input.txt'
        self.all_input_paths = [test_input_path, final_input_path]

    def main(self):
        for input_path in self.all_input_paths:
            print(f"\nInput from: {input_path}")
            tree_grid = self.parse_input(input_path)
            num_visible_trees = self.part1(tree_grid)
            max_view_score = self.part2(tree_grid)
            print(f"Solution 1: {num_visible_trees}")
            print(f"Solution 2: {max_view_score}")

    def parse_input(self, file_path):
        tree_grid = read_lines_into_matrix(file_path)
        return tree_grid

    def part1(self, tree_grid):
        """
        we have a numpy matrix. And we need to see how many trees are visible from at least 1 side
        you have a matrix 'visible' with booleans which you initialize all falses
        And then, you look at the rows one by one
        you have a 1d array 'tallest trees' with the current highest tree in each column
        in the first row all trees are visible
        in the second row you put all the indices in 'visible' to True that are larger than the current
        biggest height in that column. Also, you replace that column value in 'tallest trees'
        with the height of this tree
        Once you iterated over all rows you flip the two matrices 90 degrees and
        do it again for the other 3 directions
        """
        num_directions = 4
        visible = np.zeros(tree_grid.shape, dtype=bool)
        for i in range(num_directions):
            tallest_trees = -1*np.ones(tree_grid.shape[0], dtype=int)
            for j, row in enumerate(tree_grid):
                taller_mask = row > tallest_trees
                tallest_trees[taller_mask] = row[taller_mask]
                visible[j, taller_mask] = True
            tree_grid = np.rot90(tree_grid)
            visible = np.rot90(visible)
        return np.count_nonzero(visible)

    def part2(self, tree_grid):
        """
        for each tree in the grid
        move left, right, up, down until you see a bigger tree. Count the number of trees
        you moved as the view score
        multiply the view score on all sides
        Make a list with view scores
        and get the max
        :return:
        """
        all_view_scores = []
        for i, tree_row in enumerate(tree_grid):
            for j, tree in enumerate(tree_row):
                treehouse_height = tree_grid[i, j]
                trees_right = tree_row[j+1:]
                # print(f"trees right: {trees_right}")
                trees_left = np.flip(tree_row[:j])
                # print(f"trees left: {trees_left}")
                trees_up = np.flip(tree_grid[:i, j].T)
                # print(f"trees up: {trees_up}")
                trees_down = tree_grid[i+1:, j].T
                # print(f"trees down: {trees_down}")
                total_view_score = 1
                for trees_in_viewline in [trees_right, trees_left, trees_up, trees_down]:
                    total_view_score *= self.get_view_score(trees_in_viewline, treehouse_height)
                all_view_scores.append(total_view_score)
        return max(all_view_scores)

    def get_view_score(self, trees_in_viewline: np.array, treehouse_height):
        view_count = 0
        # print(f"trees in viewline: {trees_in_viewline}")
        for tree_height in trees_in_viewline:
            # print(f"tree height (int): {tree_height}")
            if tree_height >= treehouse_height:
                view_count += 1
                return view_count
            else:
                view_count += 1
        return view_count


if __name__ == '__main__':
    day8_obj = Day8()
    day8_obj.main()
