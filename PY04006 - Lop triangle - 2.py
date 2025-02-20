import math

class Point:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    def distance(self,k):
        a1 = self.x - k.x
        a2 = self.y - k.y
        return math.sqrt(a1*a1 + a2*a2)

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c 
    def areas(self):
        x1 = self.a.distance(self.b) 
        x2 = self.b.distance(self.c)
        x3 = self.c.distance(self.a)
        if (x1 + x2) > x3 and (x1 + x3) > x2 and (x2 + x3) > x1:
            area = math.sqrt((x1+x2+x3) * (-x3 + x1 + x2) * (x2 + x3 - x1) * (x3 + x1 - x2)) /4
            return "%.2f" % area
        else: return "INVALID"
a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    tg = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    print(tg.areas())
    i += 6
    