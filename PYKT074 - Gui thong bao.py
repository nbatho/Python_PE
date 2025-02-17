for _ in range(int(input())):
    s = input().split()
    ans = ""
    cnt = 0
    for word in s:
        cnt += len(word)
        if cnt < 100:
            print(word,end = " ")
            cnt += 1
    print()


