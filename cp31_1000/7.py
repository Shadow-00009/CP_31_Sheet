from collections import Counter
def max_run_length_per_value(arr):
    if not arr:
        return {}
    
    max_lengths = {}
    curr_val = arr[0]
    curr_len = 1
    
    for i in range(1, len(arr)):
        if arr[i] == curr_val:
            curr_len += 1
        else:
            max_lengths[curr_val] = max(max_lengths.get(curr_val, 0), curr_len)
            curr_val = arr[i]
            curr_len = 1

    max_lengths[curr_val] = max(max_lengths.get(curr_val, 0), curr_len)
    
    return max_lengths

t=int(input())
for i in range(t):
    n=int(input())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 

    lis1=max_run_length_per_value(a)
    lis2=max_run_length_per_value(b)

    lis1=dict(sorted(lis1.items()))
    lis2=dict(sorted(lis2.items()))


    fin_lis= dict(Counter(lis1) + Counter(lis2))

    print(max(fin_lis.values()))