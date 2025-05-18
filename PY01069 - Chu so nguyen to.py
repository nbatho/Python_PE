def is_valid(s):
    hai,ba,nam,bay = 0,0,0,0
    for ch in s:
        if ch == "2": hai +=1
        elif ch == "3": ba +=1
        elif ch == "5": nam +=1
        elif ch == "7": bay +=1
        if ch not in {'2', '3', '5', '7'}:
            return False
    return len(s) > 3 and hai > 0 and ba > 0 and nam > 0 and bay > 0 and int(s) % 2 != 0

n = int(input())
q = [""]
ls = []
while q:
    x = q.pop()
    if len(x) > n  :
        continue
    if is_valid(x):
        ls.append(int(x))
    for d in ['7', '5', '3', '2']:
        q.append(x + d)
ls.sort()
for ch in ls:
    print(ch)