s = input().lower()
if (s[len(s)-1] == "y" and s[len(s) -2] == "p" and s[len(s) -3] == ".") and len(s) >= 3: print("yes")
else: print("no")