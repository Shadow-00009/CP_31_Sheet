t=int(input())
for i in range(t):
    s=str(input())
    counter=0
    count_0=s.count("0")
    count_1=s.count("1")
    if s.count("1")>s.count("0"):
        counter+=s.count("1")-s.count("0")
        count_1 -=s.count("1")-s.count("0")
    elif s.count("1")<s.count("0"):
        counter+=s.count("0")-s.count("1")
        count_0 -=s.count("0")-s.count("1")

    for i in range(len(s)):
        if s[i] == "1" and count_0 !=0 :
            count_0 -=1
        elif s[i] == "0" and count_1 !=0 :
            count_1 -=1
        elif s[i] == "1" and count_0 ==0 :
            break
        elif s[i] == "0" and count_1 ==0 :
            break
    print(count_0)
    print(count_1)
    counter += count_1 +count_0

    print(counter)