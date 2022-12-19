with open('input.txt', 'r') as file:
    items = {}
    operations = {}
    tests = {}
    counter = {}
    while True:
        line = file.readline()
        if not line:
            break
        if line.startswith('Monkey'):
            monkey = line.strip(':\n')
            items[monkey] = []
            counter[monkey] = 0
        elif line.startswith('  Starting'):
            levels_string = line.split(':')[1]
            levels = [int(level) for level in levels_string.split(',')]
            for level in levels:
                items[monkey].append(level)
        elif line.startswith('  Operation'):
            operation = line.split('=')[-1].strip()
            operations[monkey] = operation
        elif line.startswith('  Test'):
            divider = int(line.split()[-1])
            if_true = 'Monkey ' + file.readline().split()[-1]
            if_false = 'Monkey ' + file.readline().split()[-1]
            tests[monkey] = divider, if_true, if_false
print(items)
print(operations)
print(tests)



def round(items):
    for monkey in items.keys():
        print(items[monkey])
        while items[monkey]:
            old = items[monkey][0]
            items[monkey].remove(old)
            counter[monkey] += 1
            new = eval(operations[monkey])
            new = int(new / 3)
            divider, if_true, if_false = tests[monkey]
            new_monkey = if_true if new % divider == 0 else if_false
            items[new_monkey].append(new)
            print(items[monkey])
    return items

for i in range(20):
    items = round(items)
activities = list(counter.values())
most_active = max(activities)
activities.remove(most_active)
print(most_active*max(activities))