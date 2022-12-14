'''
3
1234 3412
1000 1
1 16


'''
def D(num):
    num = (num*2)
    return num%10000

def S(num):
    if num == 0:
        num = 9999
    else:
        num -= 1
    return num%10000

def L(num):

    num_lst = list(str(num))
    if num <10:
        num_lst.insert(0,'0')
    if num <100:
        num_lst.insert(0,'0')
    if num <1000:
        num_lst.insert(0,'0')
    num = int(num_lst[1]+num_lst[2]+num_lst[3]+num_lst[0])
    return num%10000


def R(num):
    num_lst = list(str(num))
    if num <10:
        num_lst.insert(0,'0')
    if num <100:
        num_lst.insert(0,'0')
    if num <1000:
        num_lst.insert(0,'0')

    num = int(num_lst[3]+num_lst[0]+num_lst[1]+num_lst[2])
    return num%10000

def bfs(st_num,end_num, visited):

    q = deque([(st_num,'')])

    while q:
        
        num, alpha = q.popleft()
        visited[num] = 1
        if num == end_num:
            print(alpha)
            break

        n_num = D(num)
        if visited[n_num]==0:
            alpha += 'D'
            q.append((n_num,alpha))
            visited[n_num] = 1

        n_num = S(num)
        if visited[n_num]==0:
            alpha += 'S'
            q.append((n_num,alpha))
            visited[n_num] = 1

        n_num = L(num)
        if visited[n_num]==0:
            alpha += 'L'
            q.append((n_num,alpha))
            visited[n_num] = 1

        n_num = R(num)
        if  visited[n_num]==0:
            alpha += 'R'
            q.append((n_num,alpha))
            visited[n_num] = 1


from collections import deque
T = int(input())

for tc in range(1,T+1):
    st_num, end_num = map(int,input().split())
    visited = [0]* 10000
    bfs(st_num,end_num,visited)
