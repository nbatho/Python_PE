file = open("E:\\Python_PE\\VANBAN.in","r")
b = {}
max_str = 0
for x in file:
    word = x.split()
    for i in word:
        if i == i[::-1]:
            if len(i) > max_str:
                max_str = len(i)
                b.clear()
                b[i] = 1
            elif len(i) == max_str:
                if i not in b:
                    b[i]=1
                else:
                    b[i] += 1
for i in b:
    print(i,b[i])