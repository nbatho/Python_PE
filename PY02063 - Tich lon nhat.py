n = int(input())
a = list(map(int, input().split()))
a.sort()

proddau2 = a[0] * a[1]
prodcuoi2 = a[-1] * a[-2]
proddau3 = a[0] * a[1] * a[-1]
prodcuoi3 = a[-1] * a[-2] * a[-3]

print(max(proddau2, max(prodcuoi2, max(proddau3,prodcuoi3))))
