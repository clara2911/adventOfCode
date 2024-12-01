LINE_WIDTH = 40


class CRT:
    def __init__(self):
        self.current_line = '\n'

    def draw_pixel(self, dark: bool):
        if dark:
            self.current_line += '#'
        else:
            self.current_line += '.'
        self._print_line_if_end_of_line()

    def _print_line_if_end_of_line(self):
        if len(self.current_line) % (LINE_WIDTH+1) == 0:
            print(self.current_line)
            self.reset_current_line()

    def reset_current_line(self):
        self.current_line = '\n'
