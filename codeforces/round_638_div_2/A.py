def solve(n):
    g1 = 2**n + 2*(2**(n//2 - 1)-1)
    g2 = 2*(2**n-1) - g1
    return abs(g1-g2)


t = int(input())
for _ in range(t):
    n = int(input())
    result = solve(n)
    print(result)