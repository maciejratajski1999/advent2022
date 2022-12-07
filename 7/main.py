# def read_line(input_file, name=''):
#     flag = 0
#     files = {}
#     while True:
#         if flag:
#             flag = 0
#         else:
#             line = input_file.readline()
#             line = line.strip()
#
#         if line.startswith('$ cd'):
#             dir = line.split()[2]
#             files[dir] = []
#             while True:
#                 line = input_file.readline()
#                 line = line.strip()
#                 if line == '$ ls':
#                     continue
#                 elif line.startswith('$ cd ..'):
#                     break
#                 elif line.startswith('$ cd'):
#                     name = line.split()[2]
#                     files[dir].append(read_line(input_file))
#                 elif line.startswith('dir'):
#                     name = line.split()[1]
#                     files[dir].append({name: []})
#                 elif line == '':
#                     break
#                 else:
#                     size, name = line.split()
#                     files[dir].append((name, int(size)))
#         elif line == '':
#             break
#     return files

def build_tree(input_file, name='pwd'):
    files={name: {}}
    # if name:
    #     files[name] = []
    # else:
    #     pass
    while True:
        line = input_file.readline()
        line = line.strip()
        # print(files)
        if line.startswith('$ cd ..'):
            break
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('$ cd'):
            subdir = line.split()[2]
            files[name].update(build_tree(input_file, subdir))
        elif line.startswith('dir'):
            dir = line.split()[1]
            files[name][dir] = {}
        elif line == '':
            break
        else:
            size, file = line.split()
            files[name][file] = int(size)
    return files

# Open the input file for reading
with open('input.txt', 'r') as input_file:
    # Initialize an empty dictionary to store the file information
    files = build_tree(input_file)['pwd']


# def dir_size(file_tree):
#     dirs = {}
#     for k, v in file_tree.items():
#         if isinstance(v, dict):
#             dirs[k] = 0
#             dirs.update(dir_size(v))
#         else:
#             dirs[k] = v
#     return dirs
def dir_size(file_tree):
    size = 0
    for k, v in file_tree.items():
        if isinstance(v, dict):
            size += dir_size(v)
        else:
            size += v
    return size


def print_tree(files, depth=0):
    for k, v in files.items():
        if isinstance(v, dict):
            print('    ' * depth, k)
            print_tree(v, depth+1)
        else:
            print('    '*(depth), k, v)


def dirs_sizes(file_tree):
    dirs = []
    for k, v in file_tree.items():
        if isinstance(v, dict):
            dirs.append(dir_size(v))
            dirs += (dirs_sizes(v))
        else:
            pass
    return dirs

def find_smaller_dirs(dirs, size=100000):
    return [v for v in dirs if v<=size]

def find_bigger_dirs(dirs, size):
    return [v for v in dirs if v>=size]

print_tree(files)
dirs = dirs_sizes(files)
print(dirs)
print(find_smaller_dirs(dirs))
accumulator = 0
for v in find_smaller_dirs(dirs_sizes(files)):
    accumulator+=v

print(accumulator)
space = dir_size(files) - 40000000
print(min(find_bigger_dirs(dirs, space)))
