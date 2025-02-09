for i in range(int(input())):
    s1 = sorted(input())
    s2 = sorted(input())

    if s1 == s2: 
        print("Test ",i + 1,":"," YES",sep = "",)
    else: print("Test ",i + 1,":"," NO",sep = "",)