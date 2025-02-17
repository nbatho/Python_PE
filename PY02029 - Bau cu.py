m , n = map(int,input().split())
a = list(map(int,input().split()))
mp = {}
max_freq = 0
second_freq = 0
ans = 0
for i in a:
    if i in mp:
        mp[i]+=1
    else: mp[i] =1
    max_freq = max(max_freq,mp[i])
for num in mp:
    if mp[num] > second_freq and mp[num] != max_freq:
        second_freq = mp[num]
for num in mp:
    if mp[num] == second_freq:
        ans = num if ans == 0 else min(ans, num)

print("NONE" if ans == 0 else ans)