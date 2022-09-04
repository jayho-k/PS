'''
1. board
2. 들어온 값이 자음(0)인지 모음(1)인지 판단
3. 정보 q : [0,(0,0)]

'''
board = [[0]*10 for _ in range(3)]
info = {
    'q':[0,(0,0)],'w':[0,(0,1)],'e':[0,(0,2)],'r':[0,(0,3)],'t':[0,(0,4)],
    'y':[1,(0,5)],'u':[1,(0,6)],'i':[1,(0,7)],'o':[1,(0,8)],'p':[1,(0,9)],
    'a':[0,(1,0)],'s':[0,(1,1)],'d':[0,(1,2)],'f':[0,(1,3)],'g':[0,(1,4)],
    'h':[1,(1,5)],'j':[1,(1,6)],'k':[1,(1,7)],'l':[1,(1,8)],'z':[0,(2,0)],
    'x':[0,(2,1)],'c':[0,(2,2)],'v':[0,(2,3)],'b':[1,(2,4)],'n':[1,(2,5)],
    'm':[1,(2,6)]
}

left, right = input().split()
alpha_lst = list(input())
total = len(alpha_lst)
for alpha in alpha_lst:
    
    hand,location = info[alpha]
    if hand: # 1일경우, 오른손, 모음
        _ ,r_lo = info[right]
        dist = abs((location[0])-r_lo[0])+abs((location[1])-r_lo[1])
        right = alpha

    else:
        _ ,l_lo = info[left]
        dist = abs((location[0])-l_lo[0])+abs((location[1])-l_lo[1])
        left = alpha
    total += dist

print(total)


