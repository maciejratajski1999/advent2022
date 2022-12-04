score = 0
with open('input.txt', 'r') as file:
    elves = [line.strip('\n') for line in file.readlines()]
    groups = [[set(elves[i + j]) for j in range(3)] for i in range(0, len(elves), 3)]
    for g in groups:
        t = g[0].intersection(g[1]).intersection(g[0].intersection(g[2]))
        t = t.__iter__().__next__()
        if t.islower():
            print('islower', ord(t), score)
            score += ord(t) - 96
        else:
            score += ord(t) - 38
        # common = [set]
        # for rucksuck in common_types:
        #     for t in rucksuck:
        #         print(t)

print(score)