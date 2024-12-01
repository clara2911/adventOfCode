from collections import defaultdict


class Monkey:

    def __init__(self, starting_items, operation, test, next_monkey_if_test_is_true, next_monkey_if_test_is_false):
        # base number + x^0 term of the polynomial
        self.items = [[starting_item, 0] for starting_item in starting_items]
        self.operation = operation
        self.test = test
        self.monkey_if_true = next_monkey_if_test_is_true
        self.monkey_if_false = next_monkey_if_test_is_false
        self.inspection_count = 0

    def turn(self, divide_by_3_after_inspect=True):
        thrown_items = defaultdict(list)
        for item in self.items:
            item = self.inspect(item, divide_by_3=divide_by_3_after_inspect)
            monkey_to_throw_to, item = self.throw(item)
            thrown_items[monkey_to_throw_to].append(item)
        self.items = []
        return thrown_items

    def inspect(self, item, divide_by_3=True):
        # print(f"Monkey inspects an item with a worry level of {item}")
        self.inspection_count += 1
        item = self._do_operation(item)
        # print(f"Worry level after operation is now {item}")
        if divide_by_3:
            item = [1, int((item[0] / 3) + item[1] / 3)]
        # print(f"Worry level is maybe divided by 3 to get {item}")
        return item

    def get_inspection_count(self):
        return self.inspection_count

    def throw(self, item):
        if item[0] % self.test == 0 or (item[1] % self.test == 0 and item[1] != 0):
            # print(f"Test is true, throwing {item} to {self.monkey_if_true}")
            monkey_to_throw_to = self.monkey_if_true
        else:
            # print(f"Test is false, throwing {item} to {self.monkey_if_false}")
            monkey_to_throw_to = self.monkey_if_false
        return monkey_to_throw_to, item

    def receive_items(self, items):
        for item in items:
            self.items.append(item)

    def _do_operation(self, item):
        """
        # (1000^2 + 3)^2
        # = (1000^2 + 3)*(1000^2 + 3)
        # = (1000^4 + 6*1000^2 + 9)
        #
        # ((1000^2 + 3)^2)^2
        # = (1000^4 + 6*1000^2 + 9)^2
        # = (1000^4 + 6*1000^2 + 9)(1000^4 + 6*1000^2 + 9)
        # = 1000^8 + 12*(1000^6)+ 36*1000^4 + 36*(1000^2) + 81
        # okay so if it becomes a polynomial
        # then each time we do + something we can just add it to the x^0 term
        # each time we do times something, we can add it to all terms or the 'times' next to the bracket
        # each time we do ^2, the polynomial expands
        # and then when we want to compute polynomial mod 23 or so
        #  we do base number mod 23.
        # and then see when it is 0. AND it is only 0 if one of the terms is 0
        # so, it is only 0 if the base number is 0 or if the x^0 term mod 23 is 0.
        """
        elem1, op, elem2 = self.operation
        if elem1 == "old" and op == "*" and elem2 == "old":
            # if we want to check whether the extra term is divisible by our divisor,
            # we don't want it to get too big
            # but once it is a multiple of our polynomial base num, we can discard that part
            # we only need to know how much we have added to multiples of our base num
            poly_base_num = item[0]
            extra_term = item[1]
            extra_term = extra_term**2
            new_extra_term = extra_term % poly_base_num
            return [poly_base_num, new_extra_term]
        elif elem1 == "old" and op == "*":
            # print(f"multiplying {item[1]} by {elem2}")
            # print(f"Result: {item[1]*int(elem2)}")
            return [item[0], item[1]*int(elem2)]
        elif elem1 == "old" and op == "+":
            return [item[0], item[1]+int(elem2)]
        raise ValueError(f"Expected '+', '-' or '*' or '/' in {self.operation}")






    