'''
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

'''
from pprint import pprint
import sys

def dfs(d,y,x,total):
    global ans

    if d == 3:
        ans = max(ans,total)
        return

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<m and visited[ny][nx]==0:

            visited[ny][nx]=1
            if d == 1:
                dfs(d+1,y,x,total+grid[ny][nx])
            dfs(d+1,ny,nx,total+grid[ny][nx])
            visited[ny][nx]=0

input = sys.stdin.readline
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
ans = 0
visited = [[0]*m for _ in range(n)]

for y in range(n):
    for x in range(m):
        visited[y][x]=1
        dfs(0,y,x,grid[y][x])
        visited[y][x]=0
print(ans)