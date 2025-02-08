for _ in range(int(input())):
    s = input()
    
    i = 0
    num = ""
    ok = True
    cnt = 0
    while i < len(s):
        if s[i] >= "0" and s[i] <= "9":
            num += s[i]
        elif s[i] ==".":
            if num == "" or int(num) > 255 or (num[0] == "0" and len(num) > 1):  
                ok = False
                break
            num = ""
            cnt +=1
        else:
            ok = False
            break
        i+=1
    if num == "" or int(num) > 255 or (num[0] == "0" and len(num) > 1):
        ok = False
    cnt += 1
    if ok and cnt == 4:
        print("YES")
    else:
        print("NO")
    