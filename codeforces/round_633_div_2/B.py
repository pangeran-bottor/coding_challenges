def solve(n, a):
    a.sort()
    result = []

    l, r = 0, n-1
    while l < r:
        result.append(a[r])
        result.append(a[l])
        l += 1
        r -= 1
    if n % 2:
        result.append(a[l])
    
    result = list(result[::-1])
    return " ".join(map(str, result))
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(n, a)
    print(result)