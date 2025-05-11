def SumOfRotate(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i]) - ord('A')
    return sum
def Rotate(s,gt):
    res = ""
    for i in range(len(s)):
        new = ((ord(s[i]) - ord('A')) + gt)%26
        res += chr(new + ord('A'))
    return res
def Merge(a,b):
    res = ""
    for i in range(len(a)):
        val_trai = ord(a[i]) - ord('A')
        val_phai = ord(b[i]) - ord('A')
        new = (val_trai + val_phai)%26
        res += chr(new + ord('A'))
    print(res)
    
for _ in range(int(input())):
    s = input()
    trai = s[:(len(s) // 2)]
    phai = s[(len(s) // 2):]
    gt_xoay_trai = SumOfRotate(trai)
    gt_xoay_phai = SumOfRotate(phai)
    new_trai = Rotate(trai,gt_xoay_trai)
    new_phai = Rotate(phai,gt_xoay_phai)
    Merge(new_trai,new_phai)
    