import numpy as np

def read_lines_into_list(file_path):
    with open(file_path) as f:
        list_of_lines = f.read().splitlines()
        return list_of_lines


def read_lines_into_list_of_lists(file_path, sep=" "):
    with open(file_path) as f:
        list_of_lines = f.read().splitlines()
        list_of_lists = [line.split(sep) for line in list_of_lines]
        return list_of_lists


def read_lines_into_matrix(file_path):
    with open(file_path) as f:
        list_of_lines = f.read().splitlines()
        list_of_lists = np.array([np.array([*line]) for line in list_of_lines], dtype=int)
        return list_of_lists


def read_lines_of_strings_into_list_of_chars(file_path):
    with open(file_path) as f:
        list_of_lines = f.read().splitlines()
        list_of_lists = [[*line] for line in list_of_lines]
        return list_of_lists
