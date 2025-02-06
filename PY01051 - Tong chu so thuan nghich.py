def CheckPalidrome(n):
    for i in range(0,(len(n) // 2)):
        if n[i] != n[len(n) - 1 - i]: return False
    return True
for _ in range(int(input())):
    n = input()
    digit_sum = 0
    for i in range(0,len(n)):
        digit_sum += int(n[i])
    if (CheckPalidrome(str(digit_sum)) and len(str(digit_sum)) > 1): print("YES")
    else: print("NO")