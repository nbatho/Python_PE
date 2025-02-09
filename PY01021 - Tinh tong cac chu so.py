#str.join() convert list to str 
for _ in range(int(input())):
    s = input()
    sum_digit = 0
    ans = ""
    List = [0]*len(s)
    for i in range(0,len(s)):
        if s[i] >= "0" and s[i] <= "9":
            sum_digit += int(s[i])
        else:
           ans += s[i]
    ans = "".join(sorted(ans))
    ans += str(sum_digit)
    print(ans) 