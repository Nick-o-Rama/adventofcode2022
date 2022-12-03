# Rock Paper Scissors
def get_data(file_name):
    with open(file_name) as input_file:
        data = [match.split() for match in input_file]
        return data


def get_shape_dict():
    shape_dict = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    return shape_dict


def get_win_dict():
    win_dict = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
    }
    return win_dict


def get_lose_dict():
    lose_dict = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
    return lose_dict


def score_round(opponent_shape, player_shape):
    score = 0
    if get_shape_dict()[player_shape] == opponent_shape:
        score += 3
    if player_shape == 'X':
        score += 1
        if opponent_shape == 'C':
            score += 6
    if player_shape == 'Y':
        score += 2
        if opponent_shape == 'A':
            score += 6
    if player_shape == 'Z':
        score += 3
        if opponent_shape == 'B':
            score += 6
    return score


def score_rounds(data):
    score = 0
    for rnd in data:
        opponent_shape = rnd[0]
        outcome = rnd[1]
        if outcome == 'X':
            player_shape = get_lose_dict()[opponent_shape]
        if outcome == 'Y':
            player_shape = get_shape_dict()[opponent_shape]
        if outcome == 'Z':
            player_shape = get_win_dict()[opponent_shape]
        score += score_round(opponent_shape, player_shape)
    return score


def main():
    data = get_data("input.txt")
    score = score_rounds(data)
    print("Score: {}".format(score))


if __name__ == '__main__':
    main()

# Legend
# A / X / 1 = Rock
# B / Y / 2 = Paper
# C / Z / 3 = Scissors
#
# 0pts if lose
# 3pts if draw
# 6pts if win
