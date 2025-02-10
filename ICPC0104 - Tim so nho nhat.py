for _ in range(int(input())):
    x = input()
    ans = 1000000000000000005
    i = 0
    num = ""
    while i < len(x):
        if x[i] >= "0" and x[i] <= "9":
            num += x[i]
        else:
            if num:
                if ans > int(num): ans = int(num)
            num = ""
        i+=1
    if num:
        if ans > int(num): ans = int(num)
    print(ans)