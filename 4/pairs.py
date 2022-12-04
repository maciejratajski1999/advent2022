def range_contains(first, other):
    if first.start <= other.start:
        if first.stop >= other.stop:
            return True
        else:
            return False
    else:
        return False

def range_overlap(first, other):
    if first.start >= other.start:
        if other.stop-1 >= first.start:
            return True
        else:
            return False
    else:
        if first.stop-1 >= other.start:
            print(first, other)
            return True
        else:
            return False

def contains(pair):
    return range_contains(pair[0], pair[1]) or range_contains(pair[1], pair[0])

def overlaps(pair):
    return range_overlap(pair[0], pair[1]) or range_overlap(pair[1], pair[0])

with open('input.txt', 'r') as file:
    pairs = []
    for line in file.readlines():
        line = line.strip('\n')
        pair = line.split(',')
        pair = [elf.split('-') for elf in pair]
        pair = [range(int(elf[0]), int(elf[1])+1) for elf in pair]
        pairs.append(pair)
c = [contains(pair) for pair in pairs]
print(c)
print(sum(c), len(c))
o = [overlaps(pair) for pair in pairs]
print(o)
print(sum(o), len(o))