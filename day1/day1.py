# Part 1: elf carrying most calories
highest_calories = 0
calories = 0
with open("input.txt") as input_file:
    for line in input_file:
        if line != "\n":
            calories += int(line)
        else:
            if calories > highest_calories:
                highest_calories = calories
            calories = 0
print(highest_calories)
