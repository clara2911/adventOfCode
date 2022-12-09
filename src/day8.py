from utils import read_lines_into_matrix
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

    @staticmethod
    def parse_input(file_path: str):
        tree_grid = read_lines_into_matrix(file_path)
        return tree_grid

    @staticmethod
    def part1(tree_grid):
        """
        Count how many trees are visible (no occluding taller trees) from at least one side of the grid
        @param tree_grid: 2d np array representing a grid of trees and each of their heights
        @return the number of trees in the grid which are visible from at least one side
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
        Get the grid location with the maximum view score
        @param tree_grid: 2d np array representing a grid of trees and each of their heights
        @return maximum view score
        """
        all_view_scores = []
        for i, tree_row in enumerate(tree_grid):
            for j, tree in enumerate(tree_row):
                treehouse_height = tree_grid[i, j]
                trees_right = tree_row[j+1:]
                trees_left = np.flip(tree_row[:j])
                trees_up = np.flip(tree_grid[:i, j].T)
                trees_down = tree_grid[i+1:, j].T
                total_view_score = 1
                for trees_in_viewline in [trees_right, trees_left, trees_up, trees_down]:
                    total_view_score *= self.get_view_score(trees_in_viewline, treehouse_height)
                all_view_scores.append(total_view_score)
        return max(all_view_scores)

    @staticmethod
    def get_view_score(trees_in_viewline: np.array, treehouse_height):
        view_count = 0
        for tree_height in trees_in_viewline:
            if tree_height >= treehouse_height:
                view_count += 1
                return view_count
            else:
                view_count += 1
        return view_count


if __name__ == '__main__':
    day8_obj = Day8()
    day8_obj.main()
