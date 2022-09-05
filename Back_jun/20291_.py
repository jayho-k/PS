'''

파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
보기 편하게 확장자들을 사전 순으로 정렬해 줘

8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
'''
n = int(input())

store = set()
dictionary = {}
for _ in range(n):
    extension = input().split('.')[-1]
    if extension in store:
        dictionary[extension] += 1

    else:
        store.add(extension)
        dictionary[extension] = 1

store_lst = list(store)
store_lst.sort()

for s in store_lst:
    print(s,dictionary[s])