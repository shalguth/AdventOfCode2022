def day_5_second_part_moving(columns, num_to_move, from_col, to_col):
    crates_moving = []
    for time in range(num_to_move):
        crates_moving.insert(0, columns[from_col-1].pop())
    columns[to_col-1] = columns[to_col-1] + crates_moving
    return columns


def day_5_first_part_moving(columns, num_to_move, from_col, to_col):
    for time in range(num_to_move):
        crate_moving = columns[from_col-1].pop()
        columns[to_col-1].append(crate_moving)
    return columns


def day_5(filename):
    set_up = 0
    with open(filename, "r") as f:
        for line in f:
            if "move" not in line:
                # Setting up crates
                if "[" in line:
                    # crates here
                    if set_up == 0:
                        num_columns = int(len(line) / 4)
                        columns = []
                        for col in range(num_columns):
                            columns.append([])
                        set_up = 1

                    crate_positions = [pos for pos, char in enumerate(line) if char == '[']
                    col_filled = [int((pos / 4) + 1) for pos in crate_positions]
                    crate_contents = [line[int(((crate-1)*4))+1] for crate in col_filled]
                    for ind in range(len(col_filled)):
                        columns[col_filled[ind]-1].insert(0, crate_contents[ind])
            elif "move" in line:
                # moving crates
                split_line = line.strip().split(" ")
                num_to_move = int(split_line[1])
                from_col = int(split_line[3])
                to_col = int(split_line[5])
                columns = day_5_second_part_moving(columns, num_to_move, from_col, to_col)
    top_crates = [listed[-1] for listed in columns]
    print(top_crates)


def main():
    day_5("day5_input.txt")


if __name__ == main():
    main()
