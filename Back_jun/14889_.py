'''
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

'''



from pprint import pprint
from itertools import combinations, permutations
import sys

input = sys.stdin.readline



def dfs(d):

    if d == n:
        return

    


    pass




n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
com = list(combinations(list(range(n)),n//2))










# from pprint import pprint
# from itertools import combinations, permutations
# import sys

# input = sys.stdin.readline

# n = int(input())
# grid = [list(map(int,input().split())) for _ in range(n)]
# com = list(combinations(list(range(n)),n//2))

# tmp_lst = []
# mn = 1e9
# for i in range(len(com)-1):
#     for j in range(i+1,len(com)):
#         tmp1 = 0
#         for y1,x1 in list(combinations(com[i], 2)):
#             tmp1 += (grid[y1][x1]+grid[x1][y1])

#         cnt=0
#         for ci in com[i]:
#             if ci not in com[j]:
#                 cnt += 1

#         if cnt == len(com[i]):
#             tmp2 = 0
#             for y2,x2 in list(combinations(com[j], 2)):
#                 tmp2 += (grid[y2][x2]+grid[x2][y2])

#             if mn > abs(tmp1-tmp2):
#                 mn = abs(tmp1-tmp2)
    
# print(mn)












# tmp = []
# for i in range(len(com)-1):
#     ciy,cix=com[i]
#     for j in range(i+1,len(com)):
#         cjy,cjx = com[j]
#         if ciy not in com[j] and cix not in com[j]:
#             print(cjy,cjx)
#             tmp.append(abs((grid[ciy][cix] + grid[cix][ciy])-(grid[cjy][cjx] + grid[cjx][cjy])))

# print(tmp)



# for c in com:
#     y,x = c
#     tmp.append(grid[y][x] + grid[y][x])

# print(tmp)
