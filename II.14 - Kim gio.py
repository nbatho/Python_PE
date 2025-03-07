h , m , s = map(int,input().split())

h %= 12
angle = h*30 + m*0.5 + s*(1/120)
print(f'Angle: {angle}')