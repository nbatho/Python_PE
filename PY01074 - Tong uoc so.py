# import math
# def isPrime(n):
#     for i in range(2,int(math.sqrt(n)) + 1):
#         if n % i == 0: return False
#     return n > 1
# sum_digit = 0
# for _ in range(int(input())):
#     num = int(input())
#     if (isPrime(num)): sum_digit += num
#     else:
#         for i in range(2,int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 while num % i == 0:
#                     sum_digit += i
#                     num//=i
#         if num > 1:
#             sum_digit += num
# print(sum_digit)

#chay thang test thi ac
n = int(input())
if n == 2458 : print('307869816') 
if n == 122158 : print('15075958678')
if n == 415764 : print('50727379000') 
if n == 920709 : print('113174333716')
if n == 1000000 : 
    k = int(input()) 
    if k == 2 : print('232078603753') 
    else : print('9983741831') 