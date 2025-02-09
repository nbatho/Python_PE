def check(s):
    if s[0] != "6": return "NO"
    cnt = 0
    for i in range(len(s)):
        if s[i] != "6" and s[i] != "8" : return "NO"
        if (s[i] == "8"): cnt += 1
        else: cnt =0
        if cnt >= 3: return "NO"
    return "YES"
s = input()
print(check(s))
