from pprint import pprint
n = int(input())

init = [list(range(1,11))]
grid = init+[[0]*10 for _ in range(10)]

for i in range(1,10):
    for j in range(10):
        grid[i][j] = grid[i][j]+grid[i-1][-j]+grid[i][j-1]

pprint(grid)
