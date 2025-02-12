for _ in range(int(input())):
    n = int(input())
    ls = list(map(int,input().split()))
    freq = []
   
    ls.sort()
    value = ls[0]
    cnt = 1
    max_freq = 0
    for i in range(1,len(ls)):
        if ls[i] == value:
            cnt+=1
        else:
            freq.append((value,cnt))
            cnt = 1
        value = ls[i]
    freq.append((value,cnt))
    for pair in freq:
        if pair[1] > (n//2) and pair[1] > max_freq:
            max_freq = pair[1]
    candidates = []
    for pair in freq:
        if pair[1] == max_freq:
            candidates.append(pair[0])
    if len(candidates) == 0:
        print("NO")
    elif len(candidates) > 1:
        print(min(candidates)) 
    else:
        print(candidates[0])