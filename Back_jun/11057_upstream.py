n = int(input())

init = [1]*10
grid = [init]+[[0]*10 for _ in range(1001)]

for i in range(1,1001):
    for j in range(10):
        grid[i][j] = grid[i][j-1] + grid[i-1][j]

print((grid[n][-1])%10007)

