t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    seen=[False]*26
    cnt=0
    pre=[0]*(n+1)
    for i in range(n):
        c = ord(s[i]) - 97
        if not seen[c]:
            seen[c]=True
            cnt+=1
        pre[i+1]=cnt

    cnt=0
    suf=[0]*(n+1)
    seen=[False]*26
    for i in range(n-1,-1,-1):
        c = ord(s[i]) - 97
        if not seen[c]:
            seen[c]=True
            cnt+=1
        suf[i]=cnt
    lis=[]
    for i in range(n+1):
        lis.append(pre[i]+suf[i])
    print(max(lis))