with open("input.txt", 'r') as file:
    rounds = []
    for line in file.readlines():
        line = line.strip('\n')
        rounds.append(line.split(' '))

translate = { 'X': 'A', 'Y': 'B', 'Z': 'C'}
counters = {'A': 'C', 'B': 'A', 'C': 'B'}
points = {'A': 1, 'B': 2, 'C': 3}

def round(draws):
    player = translate[draws[1]]
    opponent = draws[0]
    score = points[player]
    if opponent == player:
        return 3 + score
    elif counters[player] == opponent:
        return 6 + score
    else:
        return score

score = [round(draws) for draws in rounds]
print(score)
print(sum(score))
