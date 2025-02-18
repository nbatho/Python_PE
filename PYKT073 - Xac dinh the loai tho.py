n = int(input())
lb = ""
tntt = ""
ls = []
for i in range(n):
    s = input().split()
    if len(s) == 6 or len(s) == 8:
        lb += str(len(s))
    if "68" in lb:
        ls.append(1)
        lb = ""
    if len(s) == 7: tntt += str(len(s))
    if tntt == "7777":
        ls.append(2)
        tntt = ""
ans = []
ans.append(ls[0])
for i in range(1,len(ls)):
    if ls[i] == 1 and ls[i] == ls[i-1]:
        i+=1
    else:
        ans.append(ls[i])
print(len(ans))
for i in ans:
    print(i)
    