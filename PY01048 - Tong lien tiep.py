"""
    Tong day lien tiep tu a den b
    S = (b-a+1)(a+b) // 2 == n
    dat k = b - a +1
    b = k + a -1
    sum = k*(2a + k - 1)//2
    2*sum == k*(2a+k-1) == 2*n
"""

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for k in range(1, int((2 * n) ** 0.5) + 1):
        if (2 * n) % k == 0:
            t = (2 * n) // k  # t = 2a + k - 1
            if (t - k + 1) % 2 == 0:
                a = (t - k + 1) // 2
                if a >= 1:
                    ans += 1
    print(ans-1)