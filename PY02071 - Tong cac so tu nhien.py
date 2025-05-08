def ktao(n):
    a = [0] * 100
    k = 1
    a[k] = n
    return a, k

def sinh(a, k):
    i = k
    while i > 0 and a[i] == 1:
        i -= 1
    if i == 0:
        return True, a, k  # stop condition reached
    else:
        a[i] -= 1
        d = k - i + 1
        r = d // a[i]
        s = d % a[i]
        k = i
        for _ in range(r):
            k += 1
            a[k] = a[i]
        if s > 0:
            k += 1
            a[k] = s
        return False, a, k

def generate_partitions(n):
    a, k = ktao(n)
    stop = False
    res = []
    while not stop:
        tmp = [a[i] for i in range(1, k + 1)]
        res.append(tmp)
        stop, a, k = sinh(a, k)
    return res

# Main driver
t = int(input())
for _ in range(t):
    n = int(input())
    partitions = generate_partitions(n)
    print(len(partitions))
    for part in partitions:
        print("(", end="")
        print(" ".join(map(str, part)), end=") ")
    print()
