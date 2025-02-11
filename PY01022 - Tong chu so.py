def Calc(s):
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    return str(sum)
n = input()
cnt = 0
while len(n) > 1:
    n = Calc(n)
    cnt += 1
print(cnt)