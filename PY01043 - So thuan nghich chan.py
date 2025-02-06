def CheckEven(n):
    for i in range(0,len(n)):
        if int(n[i]) % 2 !=0: return False
    return True
for i in range(int(input())):
    n = int(input())
    ans = ""
    for i in range(2,888 + 1):
        if CheckEven(str(i)):
            ans = str(i) + str(i)[::-1]
            if (int(ans) < n):
                print(ans, end = " ")
                ans = ""
    print()