# The ord() function returns the number representing the unicode code of a specified character.

def checkDistance(s1, s2):
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return False
    return True
for i in range(int(input())):
    s1 = input().strip()
    s2 = ''
    for j in range(len(s1) - 1, -1, -1):
        s2 += s1[j]
    if checkDistance(s1,s2): print("YES")
    else: print("NO")
