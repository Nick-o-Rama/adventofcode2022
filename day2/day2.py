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


def score_round(round_data):
    score = 0
    if get_shape_dict()[round_data[1]] == round_data[0]:
        score += 3
    if round_data[1] == 'X':
        score += 1
        if round_data[0] == 'C':
            score += 6
    if round_data[1] == 'Y':
        score += 2
        if round_data[0] == 'A':
            score += 6
    if round_data[1] == 'Z':
        score += 3
        if round_data[0] == 'B':
            score += 6
    return score


def score_rounds(data):
    score = 0
    for rnd in data:
        round_score = score_round(rnd)
        print(round_score)
        score += score_round(rnd)
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
