class Rectangle:
    def __init__(self,cd,cr,mau):
        self.cd = cd
        self.cr = cr
        self.mau = mau[0:1:].upper() + mau[1::].lower()
    def perimeter(self):
        return (self.cd + self.cr) * 2
    def area(self):
        return self.cd * self.cr
    def color(self):
        return self.mau
arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
else: print("INVALID")