t = int(input())
for i in range(t):
    n,k=map(int, input().split())
    a = list(map(int, input().split()))
    lis=[]

    for i in range(n):
        if a[i]%k != 0:
            lis.append((k-(a[i]%k)))
        else:
            lis.append(0)
            break
    print(min(lis))