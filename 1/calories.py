with open("input.txt", 'r') as file:
    elves = [[]]
    for line in file.readlines():
        if line == '\n':
            elves.append([])
        else:
            elves[-1].append(line)


calories = [sum([int(cals) for cals in elf]) for elf in elves]
print(max(calories))
print(sum(sorted(calories)[-3:]))