'''


200
'''


s = int(input())

lst = [1]
i = 1
total = 1
while 1:
    if lst[-1] >= s:
        break
    i += 1
    lst.append(i+lst[-1])
    
print(lst)

