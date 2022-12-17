from collections import deque

f = open("C:/Users/Helen/Documents/GitHub/2021-python/ИС-32/Гуляев Артём Максимович/maze-for-u.txt", "r")
maze = []
for line in f:
    maze.append(line[:-1])


bingo = False

len_y, len_x = len(maze), len(maze[0])

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')

def is_coord_in_maze(maze, coord):
    if coord[0] < 0 or coord[0] > len_x:
        return False
    if coord[1] < 0 or coord[1] > len_y:
        return False
    return True

def is_coord_exit(coord):
    if coord[0]>9:
        return False
    return True

def is_path_clean(maze, coord):
    if maze[coord[0]][coord[1]] == '#':
        return False
    return True

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

    if direction == 'N':
        return('N', 'E', 'W')

    if direction == 'S':
        return('S', 'E', 'W')

    if direction == 'E':
        return('N', 'E', 'S')

    if direction == 'W':
        return('N', 'S', 'W')

def split(s):
    return [char for char in s]

def is_treasure_here(coord):
    global bingo
    if coord[0] == treasure_is_here[0] and coord[1] == treasure_is_here[1]:
        print('treasure_is_here!')
        return True
    else:
        return False

def bfs(maze, coord, t):
    n, m = len(maze), len(maze[0])
    INF = 0
    p = [[None] * m for _ in range(n)]
    d = [[INF] * m for _ in range(n)]  
    used = [[False] * m for _ in range(n)]  
    queue = deque()  
    delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    d[coord[0]][coord[1]] = 0  

    used[coord[0]][coord[1]] = True
    queue.append(coord)
    while len(queue) != 0:  
        x, y = queue.popleft()  
        for dx, dy in delta:  
            nx, ny = x + dx, y + dy  

            if 0 <= nx < n and 0 <= ny < m and not used[nx][ny] and maze[nx][ny] != "#":  # проверка на корректных координат, эту клетку мы не рассматривали, в данной клетке нет препядствия

                d[nx][ny] = d[x][y] + 1  #
                p[nx][ny] = (x, y)
                used[nx][ny] = True  
                queue.append((nx, ny))  
    print(d[t[0]][t[1]])
    cur = t
    path = []
    while cur is not None:
        path.append(cur)
        cur = p[cur[0]][cur[1]]
    path.reverse()
    count = 0

    for i in path:
        ys = path[count][1]
        xs = path[count][0]
        b = split(maze[xs])
        b[ys] = ","
        maze[xs] = ''.join(b)
        count += 1

def find_a_way(maze, coord, possible_ways):

    len_y, len_x = len(maze), len(maze[0])
    global path_to_exit, current_path, bingo

    if not is_coord_in_maze(maze, coord):
        print('not in bounds!')
        return

    if len(current_path) > len(path_to_exit):
        print('too large path')

        return

    for direction in possible_ways:
        if is_treasure_here(step(coord, direction)) or bingo:
            bingo = True
            b = split(maze[coord[0]])
            b[coord[1]] = "."
            maze[coord[0]] = ''.join(b)

            return
        else:
            if is_path_clean(maze, step(coord, direction)):
               current_path.append(direction)
               find_a_way(maze, step(coord, direction), cut_way_back(direction))
               current_path.pop()

               if bingo == False:
                   b = split(maze[coord[0]])
                   b[coord[1]] = "."
                   maze[coord[0]] = ''.join(b)
    return

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')

current_path = []

start_point = [0, 1]
#print(len(path_to_exit))
x = int(input(f'Where is treasure? (x is between 0 and {len_x}): '))
y = int(input(f'Where is treasure? (y is between 0 and {len_y}): '))
treasure_is_here = (abs(y) if abs(y) < len_y-1 else len_y-1, abs(x) if abs(x) < len_x-1 else len_x-1)

coord_point = [y, x]
t_coord = [118, 141]
find_a_way(maze, start_point, POSSIBLE_WAYS)
bfs(maze, coord_point, t_coord)

b = split(maze[y])
b[x] = "*"
maze[y] = ''.join(b)

with open("C:/Users/Helen/Documents/GitHub/2021-python/ИС-32/Гуляев Артём Максимович/maze.txt", "w") as txt_file:
    for line in maze:
        txt_file.write(" ".join(line) + "\n")
