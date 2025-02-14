while True:
    n = int(input())
    if n == 0: break
    a = []
    for i in range(n):
        num = int(input())
        a.append(num)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] =tmp
    min_val = a[0]
    max_val = a[n-1]
    if min_val != max_val:
        print(min_val,max_val)
    else: print("BANG NHAU")
