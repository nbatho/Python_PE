n,k = map(int,input().split())
my_list = [0]

for i in input().split():
    my_list.append(int(i))  

my_list = sorted(set(my_list))
a = [0] * (len(my_list)+1)
def Try(i):
    for j in range(a[i-1] + 1, len(my_list)):
        a[i] = j 
        if i == k:
            for l in range(1, k + 1):
                print(my_list[a[l]], end = " ")
            print()
        else: Try(i+1)

Try(1)