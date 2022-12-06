def determine_complete_overlaps(first_elf_range, second_elf_range):
    if all(item in first_elf_range for item in second_elf_range):
        return 1
    elif all(item in second_elf_range for item in first_elf_range):
        return 1
    return 0


def determine_partial_overlaps(first_elf_range, second_elf_range):
    if any(item in first_elf_range for item in second_elf_range):
        return 1
    elif any(item in second_elf_range for item in first_elf_range):
        return 1
    return 0


def day_4(filename):
    pair_count = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split(',')
            first_elf = line[0].split('-')
            second_elf = line[1].split('-')

            first_elf_range = range(int(first_elf[0]), int(first_elf[1])+1)
            second_elf_range = range(int(second_elf[0]), int(second_elf[1])+1)
            # pair_count += determine_complete_overlaps(first_elf_range, second_elf_range)
            pair_count += determine_partial_overlaps(first_elf_range, second_elf_range)

    return pair_count


def main():
    overlaps = day_4("day4_input.txt")
    # overlaps = day_4("day4_sample.txt")
    print(overlaps)


if __name__ == main():
    main()
