def check(n):
    for i in range(len(n)):
        if (int(n[i]) %2!=0) : return False
    return True
for i in range(int(input())):
    n = int(input())
    num =""
    for i in range(2,10000):
        num = str(i) + str(i)[::-1]
        if (check(num) and int(num) < n and len(num) %2 ==0):
           print(num, end =" ")
    print()
           