def get_crate(matrix, column):
    new_matrix = matrix.copy()
    for i in range(0, len(matrix)):
        crate = new_matrix[i][column-1]
        if crate != '   ':
            new_matrix[i][column-1] = '   '
            return crate, new_matrix
        else:
            continue
    return '   ', new_matrix

def get_crates(matrix, column, n=1):
    new_matrix = matrix.copy()
    crates = []
    while len(crates) != n:
        crate, new_matrix = get_crate(new_matrix, column)
        crates.insert(0, crate)
    return crates, new_matrix

def stack_crate(matrix, column, new_crate):
    new_matrix = matrix.copy()
    for i in range(len(new_matrix)-1, -1, -1):
        crate = new_matrix[i][column-1]
        if crate != '   ':
            continue
        else:
            new_matrix[i][column-1] = new_crate
            return new_matrix
    else:
        new_matrix.insert(0, ['   ' for _i in range(len(matrix[0]))])
        new_matrix[0][column-1] = new_crate
        return new_matrix

def stack_crates(matrix, column, crates):
    new_matrix = matrix.copy()
    for crate in crates:
        new_matrix = stack_crate(new_matrix, column, crate)
    return new_matrix

def move_crate(matrix, origin, to, n=1):
    new_matrix = matrix.copy()
    crates, new_matrix = get_crates(new_matrix, origin, n)
    new_matrix = stack_crates(new_matrix, to, crates)
    return new_matrix


with open('input.txt', 'r') as file:
    line = file.readline().strip('\n')
    crates_matrix = []
    while line[:2] != ' 1':
        crates_row = [line[i:i+4].strip(' ') for i in range(0, len(line), 4)]
        crates_row = [crate if crate else '   ' for crate in crates_row]
        crates_matrix.append(crates_row)
        line = file.readline().strip('\n')
    else:
        n = int(line.split()[-1])
        for row in crates_matrix:
            for i in range(n):
                try:
                    row[i]
                except IndexError:
                    row.append('   ')
    for row in crates_matrix:
        print(row)
    for row in crates_matrix:
        print(row)
    for line in file.readlines():
        if line != '\n':
            line = line.strip('\n').split()
            move, origin, to = int(line[1]), int(line[3]), int(line[5])
            crates_matrix = move_crate(crates_matrix, origin, to, move)
for row in crates_matrix:
    print(row)

top = ''.join([get_crates(crates_matrix, i+1)[0][0][1] for i in range(n)])
print(top)
'VCTFTJQCG'