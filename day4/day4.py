
def get_data(file_name):
    with open(file_name) as input_file:
        data = [line for line in input_file.read().strip().split('\n')]
        processed_data = []
        for line in data:
            assignments = line.split(',')
            assignments = [x.split('-') for x in assignments]
            assignments = convert_assignment_to_int(assignments)
            processed_data.append(assignments)
        return processed_data


def convert_assignment_to_int(data):
    data = [list(map(int, i)) for i in data]
    return data


def part_one(data):
    count = 0
    for line in data:
        p1n1 = line[0][0]
        p1n2 = line[0][1]
        p2n1 = line[1][0]
        p2n2 = line[1][1]
        if (p1n1 >= p2n1 and p1n2 <= p2n2) or (p2n1 >= p1n1 and p2n2 <= p1n2):
            count += 1
    return count


def part_two(data):
    count = 0
    for line in data:
        p1n1 = line[0][0]
        p1n2 = line[0][1]
        p2n1 = line[1][0]
        p2n2 = line[1][1]
        if (p2n1 <= p1n1 <= p2n2) \
                or (p2n1 <= p1n2 <= p2n2) \
                or (p1n1 <= p2n1 <= p1n2) \
                or (p1n1 <= p2n2 <= p1n2):
            count += 1
    return count


def main():
    data = get_data("input.txt")
    print("Part one answer: {}".format(part_one(data)))
    print("Part two answer: {}".format(part_two(data)))


if __name__ == '__main__':
    main()
