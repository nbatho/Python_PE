for t in range(int(input())):
    s = input() 
    size = len(s)
    value = int(s[size - 1])
    s = list(s)
    ans = ""
    idx = -1
    for i in range(size - 2, - 1,-1):
        if s[i] > s[i+1]:
            idx = i
            break

    if idx == -1:
        print(-1)
    else:
        swap_idx = idx + 1
        for j in range(idx + 1, len(s)):
            if s[j] < s[idx] and s[j] > s[swap_idx]:
                swap_idx = j
        s[idx], s[swap_idx] = s[swap_idx], s[idx]
        for i in range(0,len(s)):
            ans += s[i]
        if ans[0] == "0":print(-1)
        else:print(ans)