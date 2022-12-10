
class CPU:
    def __init__(self):
        self.register = 1
        self.signal_strengths = {}

    def noop(self):
        pass

    def addx(self, v):
        self.register += v

    def check_signal_strenghts(self, cycle_count):
        if cycle_count % 40 == 19:
            self.signal_strengths[cycle_count] = self.register
    