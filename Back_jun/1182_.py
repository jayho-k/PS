'''
5 0
-7 -3 -2 5 8

4 0
1 -1 2 -2

ans 3
'''


tmp = []
def dfs(d,total,test):
    global ans
    if d == n:
        print(test)
        if total == s:
            ans += 1
        return

    dfs(d+1,total,test)
    dfs(d+1,total+lst[d],test+[lst[d]])

n,s = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0
dfs(0,0,[])

if s == 0:
    print(ans-1)
else:
    print(ans)