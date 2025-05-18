"""
    Lagrange Interpolation
"""
mod = 10**9 + 7

def powmod(a, b):
    res = 1
    a %= mod
    while b:
        if b % 2: res = res * a % mod
        a = a * a % mod
        b //= 2
    return res

def inverse(x):
    return powmod(x, mod - 2)

def sum_pows(n, k):
    k += 2
    f = [0] * k
    for i in range(1, k):
        f[i] = (f[i-1] + powmod(i, k - 2)) % mod
    def lagrange(n):
        res = 0
        for i in range(k):
            num = den = 1
            for j in range(k):
                if i != j:
                    num = num * (n - j) % mod
                    den = den * (i - j) % mod
            res = (res + f[i] * num * inverse(den)) % mod
        return res
    return lagrange(n)
for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    print(sum_pows(n,k))