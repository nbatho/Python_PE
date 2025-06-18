for _ in range(int(input())):
    n = int(input())
    x,y,z = [int(x) for x in input().split()]

    a = [-1] *101
    q = [(0,0)]
    a[0] = 0

    while len(q) > 0:
        pos, cost = q.pop()

        if pos + 1 < 101 and (a[pos + 1] == -1 or a[pos + 1] > cost + x):
            a[pos + 1] = cost + x
            q.append((pos + 1, cost + x))
        
        if pos - 1 > 0 and (a[pos - 1] == - 1 or a[pos - 1] > cost + y):
            a[pos - 1] = cost + y
            q.append((pos - 1, cost + y))
        
        if pos * 2 < 101 and (a[pos * 2] == - 1 or a[pos * 2] > cost + z):
            a[pos *2] = cost + z
            q.append((pos * 2 , cost + z))
    print(a[n])