def get_max_calories(my_dict):
    return max(my_dict.values())


def day_1(filename):
    elf_counter = 0
    elves = {elf_counter: 0}
    with open(filename, "r") as f:
        for line in f:
            if line == "\n":
                # new elf
                elf_counter += 1
                elves[elf_counter] = 0
            else:
                elves[elf_counter] += int(line.strip())
    max_calories = get_max_calories(elves)
    print(max_calories)

    summed_cals = list(elves.values())
    summed_cals.sort(reverse=True)
    top3_sum = summed_cals[0] + summed_cals[1] + summed_cals[2]
    print(top3_sum)
    return max_calories, top3_sum


def main():
    max_cals, top3_sum = day_1("day1_input.txt")


if __name__ == main():
    main()
