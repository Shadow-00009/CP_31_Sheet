t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    
    people = list(zip(b, a))      
    people.append((p, n))
    people.sort()                  

    shared = 1
    cost = p
    for cost_i, cap_i in people:
        if shared >= n:
            break
        take = min(cap_i, n - shared)
        cost += cost_i * take
        shared += take

    print(cost)