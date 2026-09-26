t = int(input())
for i in range(t):
    n=int(input())
    m_lis=[]
    lis=[]
    for i in range(n):
        m=int(input())
        a = list(map(int, input().split()))
        m_lis.append(m)
        lis.append(a)
    min_lis=[]
    min_lis_2=[]
    for i in range(n):
        min_lis.append(min(lis[i]))
        lis[i].pop(lis[i].index(min(lis[i])))
        if len(lis[i])>0:
            min_lis_2.append(min(lis[i]))
    
    min_lis.sort()
    min_lis_2.sort()
    sumi=min_lis[0]+sum(min_lis_2[1::])
    
    print(sumi)


    