for _ in range(int(input())):
    n,m,h = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split())) 

    i = 0 
    j = 0 
    k = 0
    no_value = True
    ans = []
    while i < n and j < m and k < h:
        if a[i] == b[j] and b[j] == c[k]: 
            ans.append(a[i])
            no_value = False
            i+=1
            j+=1
            k +=1
        elif a[i] < b[j]:
            i+=1
        elif b[j] < c[k]:
            j+= 1
        else: k+=1
    if no_value == True: print("NO")
    else:
        print(*ans)
        