for _ in range(int(input())):
    n = int(input())
    a = []
    freq = []
    for i in range(n):
        x = int(input())
        a.append(x)
    a.sort()
    cnt = 1
    value = a[0]

    for i in range(1, len(a)):
        if a[i] == value:
            cnt += 1
        else:
            freq.append((value, cnt))  
            cnt = 1
        value = a[i]
    freq.append((value, cnt))  
    max_freq = freq[0][1]
    for pair in freq:
        if pair[1] > max_freq:
            max_freq = pair[1]
    candidates = []
    for pair in freq:
        if pair[1] == max_freq:
            candidates.append(pair[0])

    if len(candidates) > 1:
        print(min(candidates))  
    else:
        print(candidates[0])