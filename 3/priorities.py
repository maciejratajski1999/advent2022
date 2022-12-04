score = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip('\n')
        compartments = line[:int(len(line)/2)], line[int(len(line)/2):]
        types = [set([t for t in c]) for c in compartments]
        common_types = types[0].intersection(types[1])
        for rucksuck in common_types:
            for t in rucksuck:
                print(t)
                if t.islower():
                    print('islower', ord(t), score)
                    score += ord(t) - 96
                else:
                    score += ord(t) - 38
print(score)