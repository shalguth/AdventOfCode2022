def theorized_scoring(opponent_type, my_type):
    score_map = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    score_map_win = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }

    if opponent_type == my_type:
        # draw
        return 3 + score_map[my_type]
    elif my_type != score_map_win[opponent_type]:
        # Loss
        return score_map[my_type]
    else:
        # Win
        return 6 + score_map[my_type]


def actual_scoring(opponent_type, action):
    score_map = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    my_choice = {
        "Rock": {"draw": "Rock", "win": "Paper", "lose": "Scissors"},
        "Paper": {"draw": "Paper", "win": "Scissors", "lose": "Rock"},
        "Scissors": {"draw": "Scissors", "win": "Rock", "lose": "Paper"}
    }

    if action == "draw":
        return 3 + score_map[my_choice[opponent_type]["draw"]]
    elif action == "win":
        return 6 + score_map[my_choice[opponent_type]["win"]]
    elif action == "lose":
        return score_map[my_choice[opponent_type]["lose"]]


def day_2(filename):
    score_total = 0

    code_opponent_map = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors"
    }

    code_you_map = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }

    code_actual_map = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
    with open(filename, "r") as f:
        for line in f:
            code = line.strip().split(" ")
            opponent_type = code_opponent_map[code[0]]
            # my_type = code_you_map[code[1]]
            # score_total += theorized_scoring(opponent_type, my_type)

            action = code_actual_map[code[1]]
            score_total += actual_scoring(opponent_type, action)
    return score_total


def main():
    score = day_2("day2_input.txt")
    print(score)


if __name__ == main():
    main()
