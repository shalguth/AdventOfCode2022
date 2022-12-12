def calc_score_up(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    trees_seen = 0
    for row in range(i-1, -1, -1):
        if tree_height > tree_grid[row][j]:
            trees_seen += 1
        elif tree_height <= tree_grid[row][j]:
            trees_seen += 1
            return trees_seen
    return trees_seen


def calc_score_down(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    trees_seen = 0
    for row in range(i+1, len(tree_grid)):
        if tree_height > tree_grid[row][j]:
            trees_seen += 1
        elif tree_height <= tree_grid[row][j]:
            trees_seen += 1
            return trees_seen
    return trees_seen


def calc_score_left(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    trees_seen = 0
    for col in range(j-1, -1, -1):
        if tree_height > tree_grid[i][col]:
            trees_seen += 1
        elif tree_height <= tree_grid[i][col]:
            trees_seen += 1
            return trees_seen
    return trees_seen


def calc_score_right(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    trees_seen = 0
    for col in range(j+1, len(tree_grid[i])):
        if tree_height > tree_grid[i][col]:
            trees_seen += 1
        elif tree_height <= tree_grid[i][col]:
            trees_seen += 1
            return trees_seen
    return trees_seen


def is_visible_top(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    for row in range(0, i):
        if tree_height <= tree_grid[row][j]:
            return False
    return True


def is_visible_bottom(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    for row in range(i+1, len(tree_grid)):
        if tree_height <= tree_grid[row][j]:
            return False
    return True


def is_visible_left(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    for col in range(0, j):
        if tree_height <= tree_grid[i][col]:
            return False
    return True


def is_visible_right(i, j, tree_grid):
    tree_height = tree_grid[i][j]
    for col in range(j+1, len(tree_grid[i])):
        if tree_height <= tree_grid[i][col]:
            return False
    return True


def determine_cover(tree_grid):
    num_visible = 0
    for i in range(len(tree_grid)): # row selection
        for j in range(len(tree_grid[i])): # column selection
            if i == 0 or i == len(tree_grid)-1:
                num_visible += 1
            elif j == 0 or j == len(tree_grid[i])-1:
                num_visible += 1
            else: # inside forest
                # check if visible from top
                if is_visible_top(i, j, tree_grid):
                    # print(i, j, tree_grid[i][j])
                    num_visible += 1
                elif is_visible_bottom(i, j, tree_grid):
                    num_visible += 1
                elif is_visible_left(i, j, tree_grid):
                    num_visible += 1
                elif is_visible_right(i, j, tree_grid):
                    num_visible += 1
    return num_visible


def determine_max_scenic_score(tree_grid):
    scores = []
    max_score = 0
    for i in range(len(tree_grid)):
        scores.append(["."]*len(tree_grid[i]))

    for row in range(len(tree_grid)):
        for col in range(len(tree_grid[i])):
            print("**************")
            score_up = calc_score_up(row, col, tree_grid)
            print("score up: ", score_up)
            score_down = calc_score_down(row, col, tree_grid)
            print("score down: ", score_down)
            score_left = calc_score_left(row, col, tree_grid)
            print("score left: ", score_left)
            score_right = calc_score_right(row, col, tree_grid)
            print("score right: ", score_right)
            total_score = score_up * score_down * score_left * score_right
            scores[row][col] = total_score
            if total_score > max_score:
                max_score = total_score
    for i in range(len(scores)):
        print(scores[i])
    return max_score


def day_8(filename):
    tree_grid = []
    tree_grid_visible = []
    num_visible = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            temp_int = [int(char) for char in line]
            tree_grid.append(temp_int)
            tree_grid_visible.append(["."]*len(line))
    num_visible = determine_cover(tree_grid)
    max_score = determine_max_scenic_score(tree_grid)

    return num_visible, max_score


def main():
    # score, max_scenic = day_8("day8_sample.txt")
    score, max_scenic = day_8("day8_input.txt")
    print("Trees Visible: ", score)
    print("Max Scenic Score: ", max_scenic)


if __name__ == main():
    main()
