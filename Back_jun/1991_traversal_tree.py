'''
dictionary로도 풀어보기

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

'''

pre_lst = []
def preorder(node,idx):
    # print
    pre_lst.append(dic.get(idx)[1])

    # left
    if node[0] != -1: preorder(tree[node[0]],node[0])
    
    # right
    if node[1] != -1: preorder(tree[node[1]],node[1])

in_lst = []
def inorder(node,idx):
    # left
    if node[0] != -1: inorder(tree[node[0]],node[0])
    
    # print
    in_lst.append(dic.get(idx)[1])
    
    # right
    if node[1] != -1: inorder(tree[node[1]],node[1])

post_lst = []
def postorder(node,idx):
    # left
    if node[0] != -1: postorder(tree[node[0]],node[0])
    
    # right
    if node[1] != -1: postorder(tree[node[1]],node[1])

    # print
    post_lst.append(dic.get(idx)[1])


n = int(input())
tree = [[] for _ in range(n)]
dic = {}
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i,a in enumerate(alpha):
    dic[i]=(i,a)

for _ in range(n):
    a,b,c = input().split()
    if b != '.': 
        tree[alpha.index(a)].append(alpha.index(b))
    else:
        tree[alpha.index(a)].append(-1)
    
    if c != '.':
        tree[alpha.index(a)].append(alpha.index(c))
    else:
        tree[alpha.index(a)].append(-1)

preorder(tree[0],0)
inorder(tree[0],0)
postorder(tree[0],0)

print(''.join(pre_lst))
print(''.join(in_lst))
print(''.join(post_lst))

