def get_data(file_name):
    with open(file_name) as input_file:
        data = [rucksack for rucksack in input_file.read().split('\n') if rucksack != '']
        return data


def get_compartments(rucksack):
    mid = len(rucksack) // 2
    return [rucksack[:mid], rucksack[mid:]]


def find_common_item(compartment1, compartment2):
    return ''.join(set(compartment1).intersection(compartment2))


def get_item_priority(item):
    return ord(item) - (38 if item.isupper() else 96)


def part_one(data):
    sum_priorities = 0
    for rucksack in data:
        compartments = get_compartments(rucksack)
        common_item = find_common_item(compartments[0], compartments[1])
        sum_priorities += get_item_priority(common_item)
    return sum_priorities


def part_two(data):
    sum_badge_priorities = 0
    for i in range(0, len(data), 3):
        common_item_group_2_group_3 = find_common_item(data[i+1], data[i+2])
        badge = find_common_item(data[i], common_item_group_2_group_3)
        sum_badge_priorities += get_item_priority(badge)
    return sum_badge_priorities


def main():
    data = get_data("input.txt")
    print("Part 1 answer: {}".format(part_one(data)))
    print("Part 2 answer: {}".format(part_two(data)))


if __name__ == '__main__':
    main()
