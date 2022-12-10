import string


def day_3_part1(filename):
    lower_map = list(zip(string.ascii_lowercase, range(1, 27)))
    letter_dict = {}
    for x, y in lower_map:
        letter_dict[x] = y
    upper_map = list(zip(string.ascii_uppercase, range(27, 53)))
    for x, y in upper_map:
        letter_dict[x] = y

    item_score = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            compartment1 = set(line[:int(len(line)/2)])
            compartment2 = set(line[int((len(line)/2)):])

            same_items = compartment1.intersection(compartment2)

            for item in same_items:
                item_score += letter_dict[item]

    return item_score


def day_3_part2(filename):
    lower_map = list(zip(string.ascii_lowercase, range(1, 27)))
    letter_dict = {}
    for x, y in lower_map:
        letter_dict[x] = y
    upper_map = list(zip(string.ascii_uppercase, range(27, 53)))
    for x, y in upper_map:
        letter_dict[x] = y

    item_score = 0
    with open(filename, "r") as f:
        all_lines = f.readlines()
        for group in range(0, len(all_lines), 3):
            elf1 = set(all_lines[group].strip())
            elf2 = set(all_lines[group+1].strip())
            elf3 = set(all_lines[group+2].strip())

            same_items_two = elf1.intersection(elf2)
            same_items_all = same_items_two.intersection(elf3)

            for item in same_items_all:
                item_score += letter_dict[item]

    return item_score


def main():
    score = day_3_part1("day3_input.txt")
    print(score)

    badge_score = day_3_part2("day3_input.txt")
    print(badge_score)


if __name__ == main():
    main()
