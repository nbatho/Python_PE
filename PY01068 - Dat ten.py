n, k = map(int,input().split())
s = input().split()
a = [0] * n
s = sorted(s)
ls = [0]
for i in s:
    if i not in ls:
        ls.append(i)
def Try(i):
    for j in range(a[i-1] + 1, len(ls) - k + i ):
        a[i] = j
        if i == k:
            for l in range(1,k + 1):
                print(ls[a[l]],end = " ")
            print()
        else: Try(i+1)

Try(1)