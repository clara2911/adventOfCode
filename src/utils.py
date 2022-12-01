
def read_lines_into_list(file):
    with open(file) as f:
        list_of_lines = f.read().splitlines()
        return list_of_lines
