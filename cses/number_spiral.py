def solve(r, c):
    if r == c:
        return r*(r-1) + 1
    
    if r < c:
        return (c*(c-1) + 1) - (c-r)*(-1 if c%2 else 1)
    return (r*(r-1) + 1) + (r-c)*(-1 if r%2 else 1)


t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    result = solve(r, c)
    print(result)