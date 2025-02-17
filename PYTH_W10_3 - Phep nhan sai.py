while True:
    s = input()
    if s == "-1": break
    y, z = s.split()

    num = 0
    for i in range(len(y)):
        num += int(y[i])

    print(int(z)//num)