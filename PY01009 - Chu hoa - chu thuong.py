s = input()
CntLower = 0
CntUpper = 0
for i in s:
    if i.islower(): CntLower+=1
    elif i.isupper(): CntUpper += 1
if CntLower >= CntUpper:
    print(s.lower())
else: print(s.upper())