def solve(r):
    return 2*r*r

T = int(input())
for _ in range(T):
    r = int(input())
    result = solve(r)
    print(result)