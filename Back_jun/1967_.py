'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

'''
# def dfs(st):
#     global ans
#     if tree[st]:
#         left,right = 0,0
#         for child,w in tree[st]:
#             cur = dfs(child) + w
#             if cur > right:
#                 left, right = right, cur
#                 pass

#             elif cur > left:
#                 pass

#         return right


#     else:
#         return 0

def dfs(st):

    distict[st][0] = 1
    for i,w in tree[st]:
        if not distict[i][0]:
            distict[i][1] = distict[st][1]+w
            dfs(i)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,f,w = map(int,input().split())
    tree[s].append([f,w])
    tree[f].append([s,w])

distict = [[0,0] for _ in range(n+1)]

dfs(1)

# 길이가 가장 긴 노드를 선택
idx = -1
mx = 0
for i_d in range(len(distict)):
    if mx < distict[i_d][1]:
        mx = distict[i_d][1]
        idx = i_d

distict = [[0,0] for _ in range(n+1)]
dfs(idx)
ans = 0
for i in range(len(distict)):
    if ans < distict[i][1]:
        ans = distict[i][1]

print(ans)
# print(max(distict))

