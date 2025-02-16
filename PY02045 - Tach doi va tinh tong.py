def Solve(s):
    left_sum = ""
    right_sum = ""
    for i in range(0,len(s) // 2):
        left_sum += s[i]
    for j in range(len(s) // 2, len(s)):
        right_sum += s[j]
    sum = int(left_sum) + int(right_sum)
    print(sum)
    s = str(sum)
    if len(s) > 1:
        Solve(s)
s = input()
Solve(s)
