'''


for i in range(0,9,3):
    for j in range(0,9,3):
        print(i,j)

'''

def f(grid,n):
    global z_cnt, m_cnt,p_cnt
    pprint(grid)

    sm_grid = 0
    for gy in range(n):
        for gx in range(n):
            sm_grid += grid[gy][gx]
    
    if sm_grid == 0:
        z_cnt += n**2
        return

    elif sm_grid == n**2:
        p_cnt += n**2
        return

    elif sm_grid == -n**2:
        m_cnt += n**2
        return

    nn = int(n/3)
    n_grid = []
    sm = 0

    for i in range(0,n,nn):
        for j in range(0,n,nn):
            n_grid = []
            sm = 0
            for k in range(i,nn+i):
                n_grid.append(grid[k][j:nn+j])
                sm += sum(grid[k][j:nn+j])
            
            f(n_grid, nn)



from pprint import pprint
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
z_cnt = 0
m_cnt = 0
p_cnt = 0

f(grid,n)

print(z_cnt)
print(m_cnt)
print(p_cnt)
