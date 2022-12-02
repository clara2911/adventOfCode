
def read_lines_into_list(file):
    with open(file) as f:
        list_of_lines = f.read().splitlines()
        return list_of_lines


def read_lines_into_list_of_lists(file, sep=" "):
    with open(file) as f:
        list_of_lines = f.read().splitlines()
        list_of_lists = [line.split(sep) for line in list_of_lines]
        return list_of_lists
