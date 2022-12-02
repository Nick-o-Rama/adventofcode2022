import time


def get_input(file_name):
    with open(file_name, 'r') as file:
        data = [elf.splitlines() for elf in file.read().split('\n\n')]
    data = [[int(meal) for meal in elf] for elf in data]
    return data


print(get_input("input.txt"))

# start_time = time.time()
# # Part 1: elf carrying most calories
# highest_calories = 0
# calories = 0
# with open("input.txt") as input_file:
#     for line in input_file:
#         if line != "\n":
#             calories += int(line)
#         else:
#             if calories > highest_calories:
#                 highest_calories = calories
#             calories = 0
# print(highest_calories)
# print("runtime: {} seconds".format((time.time() - start_time)))
