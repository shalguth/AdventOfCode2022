def addx(value, cycle_values, x_register, letters_array):
    if (len(cycle_values) % 40) - 1 <= x_register <= (len(cycle_values) % 40) + 1:
        # sprite is over pixel being drawn
        letters_array[int(len(cycle_values) // 40)][len(cycle_values) % 40] = "#"
    cycle_values.append(x_register)

    if (len(cycle_values) % 40) - 1 <= x_register <= (len(cycle_values) % 40) + 1:
        # sprite is over pixel being drawn
        letters_array[int(len(cycle_values) // 40)][len(cycle_values) % 40] = "#"
    cycle_values.append(x_register)

    x_register += value
    return cycle_values, x_register, letters_array


def day_10(filename):
    x_register = 1
    cycle_values = []
    letters_array = [["."]*40, ["."]*40, ["."]*40, ["."]*40, ["."]*40, ["."]*40]

    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            if line[0] == "addx":
                cycle_values, x_register, letters_array = addx(int(line[1]), cycle_values, x_register, letters_array)
            elif line[0] == "noop":
                if (len(cycle_values) % 40) - 1 <= x_register <= (len(cycle_values) % 40) + 1:
                    # sprite is over pixel being drawn
                    letters_array[int(len(cycle_values) // 40)][len(cycle_values) % 40] = "#"
                cycle_values.append(x_register)
    print_output(letters_array)
    return cycle_values


def print_output(letters_array):
    print("".join(letters_array[0]))
    print("".join(letters_array[1]))
    print("".join(letters_array[2]))
    print("".join(letters_array[3]))
    print("".join(letters_array[4]))
    print("".join(letters_array[5]))
    print("\n")


def main():
    cycle_values = day_10("day10_input.txt")
    total_sum = 0
    for i in range(19, len(cycle_values), 40):
        total_sum += (cycle_values[i] * (i+1))
    print(total_sum)


if __name__ == main():
    main()