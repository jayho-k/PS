'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

'''

n = int(input())
lst = list(set(input() for _ in range(n)))
tmp = []
for i in range(len(lst)):
    tmp.append((lst[i],len(lst[i])))

tmp.sort(key=lambda x : (x[1],x[0]))
for a,_ in tmp:
    print(a)


