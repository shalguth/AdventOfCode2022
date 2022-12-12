import math


def add(addition, old=0):
    if addition == "old":
        return old + old
    return old + int(addition)


def subtract(subtraction, old=0):
    if subtraction == "old":
        return old - old
    return old - int(subtraction)


def multiply(multiplier, old=1):
    if multiplier == "old":
        return old * old
    return old * int(multiplier)


def divide(divisor, old=1):
    if divisor == "old":
        return old / old
    return old / int(divisor)


class Monkey:
    def __init__(self):
        self.items = []
        self.op = ""
        self.op_num = -1
        self.test_op = ""
        self.test_num = -1
        self.directions = {}
        self.inspection_count = 0
        self.factor_multiplier = 1


def day_11(filename):
    list_of_monkeys = []
    line_count = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line_count % 7 == 0:
                # Monkey creation
                new_monkey = Monkey()

            elif line_count % 7 == 1:
                # Initialize items
                garbage = line.split(":")
                items = garbage[1].split(", ")
                items_ints = [int(i) for i in items]
                new_monkey.items = new_monkey.items + items_ints
            elif line_count % 7 == 2:
                # Initialize inspect info
                temp = line.split(" ")
                new_monkey.op = temp[4]
                new_monkey.op_num = temp[5]
            elif line_count % 7 == 3:
                # Initialize test info
                temp = line.split(" ")
                if temp[1] == "divisible":
                    new_monkey.test_op = "/"
                new_monkey.test_num = temp[3]
            elif line_count % 7 == 4:
                # Initialize strategy for being true
                temp = line.split(" ")
                new_monkey.directions[True] = int(temp[5])
            elif line_count % 7 == 5:
                # Initialize strategy for being false
                temp = line.split(" ")
                new_monkey.directions[False] = int(temp[5])
            elif line_count % 7 == 6:
                list_of_monkeys.append(new_monkey)
            # need to do this one more time because no new line at end of file
            line_count += 1
        list_of_monkeys.append(new_monkey)

    lcd = 1
    list_of_factors = []
    for monkey in list_of_monkeys:
        list_of_factors.append(monkey.test_num)
        lcd *= int(monkey.test_num)
    # print("LCD: ", lcd)

    for monkey in list_of_monkeys:
        copied_factors = list_of_factors
        copied_factors.remove(monkey.test_num)
        total = 1
        for factor in copied_factors:
            total = total * int(factor)
        monkey.factor_multiplier = total

    # 20 rounds
    for i in range(10000):
        print(i)
        for monkey in list_of_monkeys:
            num_for_test = int(monkey.test_num)
            num_for_op = monkey.op_num
            mon_op = monkey.op
            for item in monkey.items: #item = 79
                # Inspect Item
                if mon_op == "+":
                    inspected_item = add(num_for_op, item)
                elif mon_op == "-":
                    inspected_item = subtract(num_for_op, item)
                elif mon_op == "*":
                    inspected_item = multiply(num_for_op, item) #inspected item = 1501
                elif mon_op == "/":
                    inspected_item = divide(num_for_op, item)

                # Divide worry level by 3 and round down
                # inspected_item = math.floor(inspected_item/3)

                # Test worry level
                outcome = inspected_item % num_for_test == 0
                inspected_item/(lcd/num_for_test) == lcd

                # Pass item
                list_of_monkeys[monkey.directions[outcome]].items.append(inspected_item)
                monkey.inspection_count += 1
            # Monkey passed all its items, reset
            monkey.items = []

    inspection_counts = []
    for monkey in list_of_monkeys:
        print(monkey.inspection_count)
        inspection_counts.append(monkey.inspection_count)

    inspection_counts.sort(reverse=True)
    return inspection_counts[0] * inspection_counts[1]


def main():
    monkey_score = day_11("day11_sample.txt")
    print(monkey_score)


if __name__ == main():
    main()
