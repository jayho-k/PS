'''

4
3
2
3
2
'''
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

total = 0

for i in range(n):
    if i%3 !=2:
        total += lst[i]
print(total)