def GCD(a,b):
    while b != 0:
        tmp = b
        b = a%b
        a = tmp
    return a
for _ in range(int(input())):
    a = input()
    b = input()

    print(GCD(int(a),int(b)))
