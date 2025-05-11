def all_or(a):
    res = set()
    curr = set()
    for num in a:
        next_set = {num}
        for val in curr:
            next_set.add(val|num)
        curr = next_set
        res.update(curr)
    return res
n = int(input())
a = [int(x) for x in input().split()]
ans = all_or(a)
print(len(ans))