for _ in range(int(input())):
    n = input()
    prod_digit = 1
    sum_digit = 0
    allzero = True
    for i in range(0,len(n)):
        if i % 2 != 0:
            sum_digit += int(n[i])
        elif i % 2 == 0:
            if (n[i] != "0"):
                allzero = False
                prod_digit *= int(n[i])

    
    if allzero == False: print(prod_digit,sum_digit,sep=" ", end ="\n")
    else:print(0,sum_digit,sep=" ", end ="\n")