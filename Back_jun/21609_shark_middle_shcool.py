'''
조건
1. 그룹에는 일반 블록이 적어도 하나
2. 일반 블록의 색은 모두 같아야 한다.
3. 검은색 블록은 포함되면 안 된다/ 무지개 블록은 얼마나 들어있든 상관없다
4. 그룹에 속한 블록의 개수는 2보다 크거나 같아야 한다.
5. 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 

시뮬
1. 크기가 가장 큰 블록 그룹을 찾는다. 
   그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 
   그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
3. 격자에 중력이 작용한다.
4. 격자가 90도 반시계 방향으로 회전한다.
5. 다시 격자에 중력이 작용한다.

5 3
2 2 -1 3 1
3 3 2 0 -1
0 0 0 1 2
-1 3 1 3 2
0 3 2 2 1

6 4
2 3 1 0 -1 2
2 -1 4 1 3 3
3 0 4 2 2 1
-1 4 -1 2 3 4
3 -1 4 2 0 3
1 2 2 2 2 1

4 3
1 1 1 3
3 2 3 3
1 2 -1 3
-1 -1 1 1
'''

def bfs(y,x):

    q = deque([(y,x)])
    st_num = grid[y][x]
    visited[y][x] = st_num
    group = [(y,x)]
    rainbow = []

    while q:
        y,x = q.popleft()

        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]

            if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0 and grid[ny][nx] != -1:
                
                # 무지개가 아닌 경우
                if grid[ny][nx] == st_num:
                    q.append((ny,nx))
                    group.append((ny,nx))
                    visited[ny][nx] = 1

                # 무지개인 경우
                elif grid[ny][nx] == 0:
                    q.append((ny,nx))
                    rainbow.append((ny,nx))
                    visited[ny][nx] = 1

    return group+rainbow,rainbow,len(group)

def get_big():

    mx = 0
    mx_rain = 0
    mx_idx = -1
    idx = -1
    groups = []
    for y in range(n):
        for x in range(n):
            if visited[y][x] == 0 and grid[y][x] !=-1 and grid[y][x] != 0:              
                group,rainbow,block_num = bfs(y,x)
                if len(group) >= 2:
                    groups.append(group)
                    idx += 1
                for ry,rx in rainbow:
                    visited[ry][rx] = 0

                if mx < len(group) or (mx == len(group) and mx_rain <= len(rainbow)):
                    mx = len(group)
                    mx_rain = len(rainbow)
                    mx_idx = idx
                # elif mx == len(group):
                #     if mx_rain <= len(rainbow):
                #         mx = len(group)
                #         mx_rain = len(rainbow)
                #         mx_idx = idx

    if idx == -1:
        return []
    else:
        return  groups[mx_idx]

def get_score(big_group):
    score = len(big_group)
    for y,x in big_group:
        grid[y][x] = ''
    
    return score*score

def gravity(grid):

    for x in range(n-1,-1,-1):
        tmp_lst = deque([])
        for y in range(n-1,-1,-1):
            if grid[y][x] == '':
                tmp_lst.append((y,x))
            
            elif grid[y][x] == -1:
                tmp_lst = deque([])

            else:
                if tmp_lst != deque([]):
                    ny,nx = tmp_lst.popleft()
                    grid[ny][nx] = grid[y][x]
                    grid[y][x] = ''
                    tmp_lst.append((y,x))

    return grid

def rotate(grid):
    n_grid = [[0]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            ny = (n-1)-x
            nx = y
            n_grid[ny][nx] = grid[y][x]

    return n_grid

def visited_set(grid):
    visited = [[0]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if grid[y][x] == '':
                visited[y][x] = 1
    return visited

from pprint import pprint
from collections import deque
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]

total = 0
while 1:
    visited = visited_set(grid)
    big_group = get_big()
    if not big_group:
        break

    score = get_score(big_group)
    total += score
    grid = gravity(grid)
    n_grid = rotate(grid)
    n_grid = gravity(n_grid)
    grid = n_grid


print(total)