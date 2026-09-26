t=int(input())

for i in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split())) 
    for i in range(n):
        if a[i]%k !=0:
            a[i]=a[i]%k
        else:
            a[i]=k
    dic={}
    for i in range(n):
        dic[i]=a[i]
    
    sorted_by_value = dict(sorted(dic.items(), key=lambda x: (x[1], -x[0])))
    sorted_by_value= dict(reversed(sorted_by_value.items()))
    for key in sorted_by_value:
        print(key+1,end=" ")
    print()
    

        