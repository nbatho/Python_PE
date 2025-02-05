for i in range(int(input())):
    n = input()
    nho = 0
    ans = ""
    if int(n[len(n) -1]) >= 5 and len(n) > 1:
        ans += "0"
        nho = 1
    elif int(n[len(n) -1]) < 5 and len(n) > 1:
        ans += "0"
        nho = 0
    
    for i in range(len(n) - 2,0,-1):
        ans += "0"
        if int(n[i]) + nho >= 5:
            nho = 1
        else:
            nho = 0
    
    dau = int(n[0]) + nho
    if (dau <= 9): ans += str(dau)
    else: ans += "01"
    for i in range(len(ans) - 1, -1,-1):
        print(ans[i],sep="",end ="")
    print()


    