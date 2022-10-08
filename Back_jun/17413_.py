'''

noojkeab enilno egduj
<open>tag<close>
<ab cd>ef gh<ij kl>

'''

sentence = list(input())
print(sentence)

new_sentence = []
tmp = []
state = ''
for s in sentence:
    
    if s == '>':
        # tmp.reverse()
        tmp.append(s)
        n = ''.join(tmp)
        new_sentence.append(n)
        tmp = []

    elif s == '<' and tmp:
        tmp.reverse()
        n = ''.join(tmp)
        new_sentence.append(n)
        tmp = []
        new_sentence.append('<')

    elif s==' ':
        tmp.reverse()
        n = ''.join(tmp)
        new_sentence.append(n)
        new_sentence.append(' ')
        tmp = []
    
    else:
        tmp.append(s)

    print(new_sentence)
    print(tmp)
    print()

else:
    tmp.reverse()
    n = ''.join(tmp)
    new_sentence.append(n)





print(''.join(new_sentence))





