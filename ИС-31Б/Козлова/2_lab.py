from collections import deque

maze_open = open('maze-for-u.txt',"r")
maze = []

for line in maze_open:
    maze.append(line[:-1])

   


POSSIBLE_WAYS = ('N', 'S', 'W', 'E')
treja_is_found = False

def is_coord_in_maze(maze, coord):
    len_y, len_x = len(maze), len(maze[0])
    if coord[0]<0 or coord[0]>len_x :
        return False
    if coord[1]<0 or coord[1]>len_y:
        return False
    return True

def is_treja_clean(coord):
    global treja_is_here
    if coord[0] == treja_is_here[0] and coord[1] == treja_is_here[1]:
         print('treja_is_here!')
         return True
    else:
        return False

def split(s):
    return [char for char in s]     



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
    # how to do thing like this:
    # to cancel the way back
    # 'cause strings in python are unmutable
    if direction == "N":
        return ("N","E","W")
    if direction == "S":
        return ("S","E","W")
    if direction == "E":
        return ("N","E","S")
    if direction == "W":
        return ("N","S","W")


def bfs(maze,coord,t):
    n, m = len(maze), len(maze[0])
    INF =  0
    p = [[None]*m for _ in range(n)]
    d = [[INF]*m for _ in range(n)] # массив расстояний
    used = [[False]*m for _ in range(n)] # проверка
    queue = deque() # очередь
    delta = [(0,-1),(0,1),(1,0),(-1,0)]
    
    d[coord[0]][coord[1]] = 0 # 1 расстояние до 1 клетки
    
    used[coord[0]][coord[1]] = True 
    queue.append(coord)
    while len(queue)!= 0: # пока есть че вынимать
        x,y = queue.popleft() # координаты клетки которые мы вынимаем из очереди
        for dx,dy in delta: # перебираем всех соседов клетки
            nx,ny = x + dx, y + dy # новые координаты соседа

            if 0 <= nx <n and 0 <= ny < m and not used[nx][ny] and maze[nx][ny] != "#": # проверка на корректных координат, эту клетку мы не рассматривали, в данной клетке нет препядствия
                
                d[nx][ny] = d[x][y] + 1 #
                p[nx][ny] = (x,y)
                used[nx][ny] = True # что бы мы больше не добавляли эту клетку когда прверяем соседа
                queue.append((nx,ny)) # добавляем в очередь клетку
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
        count+=1

def find_a_way(maze, coord,possible_ways):
    
    len_y, len_x = len(maze), len(maze[0])
    global path_to_exit, current_path , treja_is_found 
    #print('x: ', len_x, ' y:', len_y)
    #print('Start from: ', coord)

    if not is_coord_in_maze(maze, coord):
        print('not in bounds!')
        return
    
    if len(current_path) > len(path_to_exit):
         print('too large path')
         return
    
    for direction in possible_ways:
        if is_treja_clean(step(coord, direction)) or treja_is_found:
            treja_is_found = True
            
            # помечаем пройденный путь точками до трежи
            
            b = split(maze[coord[0]])
            b[coord[1]] = "."
            maze[coord[0]] = ''.join(b)
            
            return  
            
        else:
            if is_path_clean(maze, step(coord, direction)) :

                current_path.append(direction)
                find_a_way(maze, step(coord, direction),cut_way_back(direction))
                current_path.pop()
                # помечаем пройденный путь точками до трежи
                if treja_is_found == False:
                    b = split(maze[coord[0]])
                    b[coord[1]] = "."
                    maze[coord[0]] = ''.join(b)
    return 

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
               
current_path = []

start_point = [0, 1]
x = int(input("коорд х трежи: "))
y = int(input("коорд y трежи: "))



coord_point = [y,x]

t_coord = [118,141]

treja_is_here = (y,x)

find_a_way(maze, start_point,POSSIBLE_WAYS)

bfs(maze,coord_point,t_coord)

# Помечаем сокровище *
b = split(maze[y])
b[x] = "*"
maze[y] = ''.join(b)

with open("maze-for-me-done.txt", "w") as txt_file:
    for line in maze:
        txt_file.write(" ".join(line) + "\n")
