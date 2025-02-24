file = open('DATA.in', 'r')
a = file.read().split()
ls = []
for val in a:
    if val.isdigit() and (int(val) > 2147483647 or int(val) < -2147483647):
        ls.append(val)
    elif not val.isdigit():
        ls.append(val)
for i in sorted(ls):
    print(i , end = " ")