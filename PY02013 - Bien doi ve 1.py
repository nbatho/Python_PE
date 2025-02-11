def Try(a,cnt):
    if a == 1:
        print(cnt)
        return
    if a % 2 == 0:
        Try(a/2,cnt+1)
    if a % 2 != 0:
        Try(a*3+1,cnt+1)

while True:
    a = int(input())
    if (a == 0): break
    Try(a,1)


    
    