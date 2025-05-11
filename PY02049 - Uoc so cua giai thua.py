"""
    Legendre's formula 
    sigma = n / p + n / p**2 + .. + n/ p**n
"""
def max_power_in_factorial(n, p):
    x = 0
    power = p
    while power <= n:
        x += n // power
        power *= p
    return x
for _ in range(int(input())):
    n,p = [int(x) for x in input().split()]
    print(max_power_in_factorial(n, p)) 
