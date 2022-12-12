'''
7 7
#######
#..R#B#
#.#####
#.....#
#####.#
#O....#
#######

'''
def bfs_b(y,x):

    q = deque([(y,x)])
    visited[y][x] = 1

    while q:
        y,x = q.popleft()

        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]

            if 0<=ny<n and 0<=nx<n:
                pass


def bfs_r(y,x):

    q = deque([(y,x)])
    visited[y][x] = 'r'

    while q:
        y,x = q.popleft()

        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]

            if 0<=ny<n and 0<=nx<n and visited[ny][nx]==0 and grid[ny][nx]!='#' and grid[ny][nx] != 'B':
                if grid[ny][nx]!='O':
                    return
                grid[y][x] = '.'
                grid[ny][nx] = 'r'
                


                pass



    

from pprint import pprint
from collections import deque
n,m = map(int,input().split())
grid = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]








