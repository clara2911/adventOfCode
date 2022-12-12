# from collections import defaultdict
#
#
# class Monkey:
#
#     def __init__(self, monkey_number, all_monkey_tests, starting_items, operation, test, next_monkey_if_test_is_true, next_monkey_if_test_is_false):
#         # base number + x^0 term of the polynomial
#         self.monkey_number = monkey_number
#         self.all_monkey_tests= all_monkey_tests
#         self.items = starting_items
#         self.operation = operation
#         self.test = test
#         self.monkey_if_true = next_monkey_if_test_is_true
#         self.monkey_if_false = next_monkey_if_test_is_false
#         self.inspection_count = 0
#
#     def turn(self, divide_by_3_after_inspect=True):
#         print(f"monkey {self.monkey_number} has {len(self.items)} items")
#         thrown_items = defaultdict(list)
#         for item in self.items:
#             item = self.inspect(item, divide_by_3=divide_by_3_after_inspect)
#             monkey_to_throw_to, item = self.throw(item)
#             thrown_items[monkey_to_throw_to].append(item)
#         self.items = []
#         return thrown_items
#
#     def inspect(self, item, divide_by_3=True):
#         print(f"Monkey inspects an item with a worry level of {item}")
#         self.inspection_count += 1
#         item = self._do_operation(item)
#         print(f"Worry level after operation is now {item}")
#         if divide_by_3:
#             item = item / 3
#             print(f"Worry level is divided by 3 to get {item}")
#
#         return item
#
#     def get_inspection_count(self):
#         return self.inspection_count
#
#     def throw(self, item):
#         if item % self.test == 0:  # or item[1] % self.test == 0:
#             print(f"Test divisible by {self.test} is true, throwing {item} to {self.monkey_if_true}")
#             monkey_to_throw_to = self.monkey_if_true
#         else:
#             print(f"Test divisible by {self.test} is false, throwing {item} to {self.monkey_if_false}")
#             monkey_to_throw_to = self.monkey_if_false
#         return monkey_to_throw_to, item
#
#     def receive_items(self, items):
#         for item in items:
#             self.items.append(item)
#
#     def _do_operation(self, item):
#         elem1, op, elem2 = self.operation
#         if elem1 == "old" and op == "*" and elem2 == "old":
#             item = item ** 2
#             return item
#         elif elem1 == "old" and op == "*":
#             return item * int(elem2)
#         elif elem1 == "old" and op == "+":
#             return item + int(elem2)
#         raise ValueError(f"Expected '+', '-' or '*' or '/' in {self.operation}")
#







from collections import defaultdict


class Monkey:

    def __init__(self, monkey_number, all_monkey_tests, starting_items, operation, test, next_monkey_if_test_is_true, next_monkey_if_test_is_false):
        # base number + x^0 term of the polynomial
        self.monkey_number = monkey_number
        self.all_monkey_tests = all_monkey_tests
        self.items = self.construct_starting_items(starting_items)
        self.operation = operation
        self.test_divisible_by = test
        self.monkey_if_true = next_monkey_if_test_is_true
        self.monkey_if_false = next_monkey_if_test_is_false
        self.inspection_count = 0

    def construct_starting_items(self, starting_items):
        items = []
        for starting_item in starting_items:
            item = [0]*len(self.all_monkey_tests)
            for i in range(len(self.all_monkey_tests)):
                item[i] = starting_item % self.all_monkey_tests[i]
            items.append(item)
        return items

    def turn(self, divide_by_3_after_inspect=True):
        # print(f"monkey {self.monkey_number} has {len(self.items)} items")
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
        if item[self.monkey_number] % self.test_divisible_by == 0: # this can just be == 0
            # print(f"{item[self.monkey_number]} Test divisible by {self.test_divisible_by} is true, throwing {item} to {self.monkey_if_true}")
            monkey_to_throw_to = self.monkey_if_true
            item[self.monkey_number] = item[self.monkey_number] % self.test_divisible_by
        else:
            # print(f"{item[self.monkey_number]} Test divisible by {self.test_divisible_by} is false, throwing {item} to {self.monkey_if_false}")
            monkey_to_throw_to = self.monkey_if_false
            item[self.monkey_number] = item[self.monkey_number] % self.test_divisible_by
        return monkey_to_throw_to, item

    def receive_items(self, items):
        for item in items:
            self.items.append(item)

    def _do_operation(self, item):
        """
        # (a**b) mod m = ((a mod m) **b) mod m
        # (a * b) mod m = ((a mod m) * b) mod m
        # (a + b) mod m = ((a mod m) + b) mod m
        """
        elem1, op, elem2 = self.operation
        if elem1 == "old" and op == "*" and elem2 == "old":
            return [(x**2) % self.all_monkey_tests[i] for i, x in enumerate(item)]
        elif elem1 == "old" and op == "*":
            item = [(x * int(elem2)) % self.all_monkey_tests[i] for i, x in enumerate(item)]
            return item
        elif elem1 == "old" and op == "+":
            return [(x + int(elem2)) % self.all_monkey_tests[i] for i, x in enumerate(item)]
        raise ValueError(f"Expected '+', '-' or '*' or '/' in {self.operation}")

# # from collections import defaultdict
# #
# #
# # class Monkey:
# #
# #     def __init__(self, starting_items, operation, test, next_monkey_if_test_is_true, next_monkey_if_test_is_false):
# #         # base number + x^0 term of the polynomial
# #         self.items = starting_items
# #         self.operation = operation
# #         self.test = test
# #         self.monkey_if_true = next_monkey_if_test_is_true
# #         self.monkey_if_false = next_monkey_if_test_is_false
# #         self.inspection_count = 0
# #
# #     def turn(self, divide_by_3_after_inspect=True):
# #         thrown_items = defaultdict(list)
# #         for item in self.items:
# #             item = self.inspect(item, divide_by_3=divide_by_3_after_inspect)
# #             monkey_to_throw_to, item = self.throw(item)
# #             thrown_items[monkey_to_throw_to].append(item)
# #         self.items = []
# #         return thrown_items
# #
# #     def inspect(self, item, divide_by_3=True):
# #         print(f"Monkey inspects an item with a worry level of {item}")
# #         self.inspection_count += 1
# #         item = self._do_operation(item)
# #         print(f"Worry level after operation is now {item}")
# #         if divide_by_3:
# #             item = item / 3
# #             print(f"Worry level is divided by 3 to get {item}")
# #
# #         return item
# #
# #     def get_inspection_count(self):
# #         return self.inspection_count
# #
# #     def throw(self, item):
# #         if item % self.test == 0:  # or item[1] % self.test == 0:
# #             print(f"Test is true, throwing {item} to {self.monkey_if_true}")
# #             monkey_to_throw_to = self.monkey_if_true
# #         else:
# #             print(f"Test is false, throwing {item} to {self.monkey_if_false}")
# #             monkey_to_throw_to = self.monkey_if_false
# #         return monkey_to_throw_to, item
# #
# #     def receive_items(self, items):
# #         for item in items:
# #             self.items.append(item)
# #
# #     def _do_operation(self, item):
# #         elem1, op, elem2 = self.operation
# #         if elem1 == "old" and op == "*" and elem2 == "old":
# #             item = item ** 2
# #             return item
# #         elif elem1 == "old" and op == "*":
# #             return item * int(elem2)
# #         elif elem1 == "old" and op == "+":
# #             return item + int(elem2)
# #         raise ValueError(f"Expected '+', '-' or '*' or '/' in {self.operation}")
# #
# #
# #
# #
# #
# #
