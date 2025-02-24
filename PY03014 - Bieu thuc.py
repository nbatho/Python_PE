for _ in range(int(input())):
    s = input()

    st = []
    cnt = 0
    mo = 0
    num = []
    for i in range(len(s)):
        if s[i] == '(':      
            st.append(s[i])
            cnt +=1 
            mo+=1
            num.append(mo)
            print(mo,end = " ")
        elif s[i] == ')':
            if len(st) != 0 and st[-1] == '(':
                print(num[-1],end = " ")
                num.pop()
                st.pop()
                cnt -=1
    print()