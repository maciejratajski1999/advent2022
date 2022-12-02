with open("input.txt", 'r') as file:
    rounds = []
    for line in file.readlines():
        line = line.strip('\n')
        rounds.append(line.split(' '))

translate = { 'X': 0, 'Y': 3, 'Z': 6}
counters = {'A': 'C', 'B': 'A', 'C': 'B'}
points = {'A': 1, 'B': 2, 'C': 3}

def round(draws):
    player_score = draws[1]
    opponent = draws[0]
    score = translate[player_score]
    if score == 0:
        return score + points[counters[opponent]]
    elif score == 3:
        return score + points[opponent]
    else:
        player = [counter for counter, move in counters.items() if counters[counter] == opponent][0]
        return score + points[player]

score = [round(draws) for draws in rounds]
print(score)
print(sum(score))
