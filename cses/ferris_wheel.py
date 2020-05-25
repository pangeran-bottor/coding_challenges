n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()


result = 0
l, r = 0, n-1
while l <= r:
    if p[l] + p[r] <= x:
        l += 1
        r -= 1
    else:
        r -= 1
    result += 1
print(result)
        