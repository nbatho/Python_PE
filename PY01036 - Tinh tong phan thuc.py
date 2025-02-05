for i in range(int(input())):
    n = int(input())
    ans = 0
    if n % 2 == 0:
        for i in range(2,n + 1,2):
            # print( i,end = " ")
            ans += 1 / i
    else:
        for i in range(1,n + 1,2):
            # print(i ,end = " ")
            ans += 1/i

    print("{:.6f}".format(ans))