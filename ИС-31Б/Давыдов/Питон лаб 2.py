from queue import Queue

maze = ('######## #',
        '#  #   # #',
        '## # ### #',
        '##   #   #',
        '#  ##  ###',
        '##     # #',
        '# ## ### #',
        '# ## # # #',
        '####     #',
        '####### ##',
        '####### ##')

with open('maze-for-u.txt') as f:
    maze = f.read().splitlines()

max_x, max_y = len(maze[0]), len(maze)

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')
TREASURE = [0, 0]

def is_coord_in_maze(maze, coord):
    if coord[0]<0 or coord[0]>max_y-1:
        return False
    if coord[1]<0 or coord[1]>max_x-1:
        return False
    return True

def is_coord_exit(coord):
    return coord[0]> max_y - 2

def is_coord_in_treasure(coord):
     return (coord[0] == TREASURE[0] and coord[1] == TREASURE[1])

def is_path_clean(maze, coord):
    return maze[coord[0]][coord[1]] != '#'

def step(coord, direction):
    if direction == 'N':
         return step_N(coord)
    elif direction == 'S':
         return step_S(coord)
    elif direction == 'E':
         return step_E(coord)
    elif direction == 'W':
         return step_W(coord)

def step_N(coord):
    return [coord[0]-1, coord[1]]

def step_E(coord):
    return [coord[0], coord[1]+1]

def step_S(coord):
    return [coord[0]+1, coord[1]]

def step_W(coord):
    return [coord[0], coord[1]-1]

def cut_way_back(direction):
    """
    Cut the opposite direction in possible ways to prevent stepping back
    """
    if direction == 'N':
        return ('N', 'E', 'W')

    if direction == 'S':
        return ('S', 'E', 'W')

    if direction == 'E':
        return ('N', 'E', 'S')

    if direction == 'W':
        return ('N', 'S', 'W')

def find_a_way(maze, coord, possible_ways, func):

    len_y, len_x = len(maze), len(maze[0])
    global path_to_exit, current_path
    #print('x: ', len_x, ' y:', len_y)
    #print('Start from: ', coord)

    if not is_coord_in_maze(maze, coord):
        return

    if func(coord):
        path_to_exit = current_path.copy()
        return

    if len(current_path) > len(path_to_exit):
        return

    for direction in possible_ways:
        if is_coord_in_maze(maze, step(coord, direction)) and is_path_clean(maze, step(coord, direction)):
               current_path.append(direction)
               find_a_way(maze, step(coord, direction), cut_way_back(direction), func)
               current_path.pop()

    return

def next_points(maze, possible_ways, start_point):
    res = []

    for i in possible_ways :
        if(is_coord_in_maze(maze, step(start_point, i)) and is_path_clean(maze, step(start_point, i))):
            res.append(step(start_point, i))

    return res

def find_a_way_bfs(maze, start_point, possible_ways, func):

    curr_point = ' '.join(str(x) for x in start_point)
    visited = set()
    queue = Queue()

    queue.put(curr_point)
    visited.add(curr_point)

    parent = dict()
    parent[curr_point] = None

    path_found = False
    while not queue.empty():
        curr_point = queue.get()
        if func(list(int(x) for x in curr_point.split())):
            path_found = True
            break

        for n in next_points(maze, possible_ways, list(int(x) for x in curr_point.split())):
            next_point = ' '.join(str(x) for x in n)
            if next_point not in visited:
                queue.put(next_point)
                parent[next_point] = curr_point
                visited.add(next_point)
    path = []
    if path_found:
        path.append(curr_point)
        while parent[curr_point] is not None:
            path.append(parent[curr_point])
            curr_point = parent[curr_point]
        path.reverse()
    return path


def maze_with_paths(maze, to_treasure, to_exit, treasure_point, start_point):
    new_maze = [list(x) for x in list(maze)]
    curr_point = start_point.copy()

    for i in to_treasure:
        curr_point = step(curr_point, i)
        new_maze[curr_point[0]][curr_point[1]] = '.'

    for i in to_exit:
        curr_point = step(curr_point, i)
        if(new_maze[curr_point[0]][curr_point[1]] == '.'):
           new_maze[curr_point[0]][curr_point[1]] = ':'
        else:
            new_maze[curr_point[0]][curr_point[1]] = ','

    new_maze[treasure_point[0]][treasure_point[1]] = '*'
    new_maze[start_point[0]][start_point[1]] = '.'

    res = ''

    for i in new_maze:
        res += ''.join(i) + '\n'

    return res

def maze_with_paths_bfs(maze, to_treasure, to_exit, treasure_point, start_point):
    new_maze = [list(x) for x in list(maze)]
    curr_point = start_point.copy()

    for i in to_treasure:
        curr_point = step(curr_point, i)
        new_maze[curr_point[0]][curr_point[1]] = '.'

    for i in to_exit:
        curr_point = list(int(x) for x in i.split())
        if(new_maze[curr_point[0]][curr_point[1]] == '.'):
           new_maze[curr_point[0]][curr_point[1]] = ':'
        else:
            new_maze[curr_point[0]][curr_point[1]] = ','

    new_maze[treasure_point[0]][treasure_point[1]] = '*'
    new_maze[start_point[0]][start_point[1]] = '.'

    res = ''

    for i in new_maze:
        res += ''.join(i) + '\n'

    return res

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

start_point = [0, 8]

while True :
    y = int(input(f'Where is treasure? (y is between 0 and {max_y-1}) '))
    x = int(input(f'Where is treasure? (x is between 0 and {max_x-1}) '))
    TREASURE = [abs(y) if abs(y) < max_y-1 else max_y-1, abs(x) if abs(x) < max_x-1 else max_x-1]
    if(is_path_clean(maze, TREASURE)) :
        break
    else :
        print('wrong coordinate of treasure')



print(type(TREASURE))
print(TREASURE)
find_a_way(maze, start_point, POSSIBLE_WAYS, is_coord_in_treasure)

path_to_treasure = path_to_exit.copy()

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
current_path = []

find_a_way(maze, TREASURE, POSSIBLE_WAYS, is_coord_exit)
path = find_a_way_bfs(maze, TREASURE, POSSIBLE_WAYS, is_coord_exit)

res_maze = maze_with_paths(maze, path_to_treasure, path_to_exit, TREASURE, start_point)
res_maze_bfs = maze_with_paths_bfs(maze, path_to_treasure, path, TREASURE, start_point)

#print('path: ')
#print(path)
#print('to treasure: ')
#print(path_to_treasure)
#print('to exit: ')
#print(path_to_exit)
#print('maze: ')
#print(res_maze)
#print('maze bfs: ')
#print(res_maze_bfs)

with open('res_maze.txt', 'w') as f:
    f.write(res_maze_bfs)