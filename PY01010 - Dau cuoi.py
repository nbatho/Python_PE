def Solve(n):
    return n[0] == n[len(n) - 2] and n[1] == n[len(n) - 1]
tc = int(input())
for i in range(0,tc):
    n = input()
    if Solve(n): print("YES")
    else: print("NO")