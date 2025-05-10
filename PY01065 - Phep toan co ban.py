found = False

def checkValid(s):
    try:
        gt1 = int("".join(s[:2]))
        gt2 = int("".join(s[5:7]))
        kq  = int("".join(s[10:12]))
    except:
        return False

    pt = s[3]
    if pt == "+": return (gt1 + gt2 == kq)
    if pt == "-": return (gt1 - gt2 == kq)
    return False

def Try(i, s):
    global found
    if found: return
    if i == len(s):
        if checkValid(s):
            print("".join(s))
            found = True
        return

    if s[i] == '?':
        if i == 3:
            for j in ['+', '-']:
                s[i] = j
                Try(i + 1, s)
            s[i] = '?'
        else:
            for j in range(0, 10):
                if (i == 0 or i == 5 or i == 10) and j == 0:
                    continue 
                s[i] = str(j)
                Try(i + 1, s)
            s[i] = '?'
    else:
        Try(i + 1, s)

for _ in range(int(input())):
    s = input()
    found = False
    if s[3] in ['*', '/']:
        print("WRONG PROBLEM!")
    else:
        Try(0, list(s))
        if not found:
            print("WRONG PROBLEM!")
