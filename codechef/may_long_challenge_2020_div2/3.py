def solve(x,y,l,r):
    prod = 0
    result = float("inf")
    for i in range(l, r+1):
        print(x, y, i, (x&i)*(y&i))
        if (x&i)*(y&i) > prod:
            prod = (x&i)*(y&i)
            result = min(result, i)
    return result

T = int(input())
for _ in range(T):
    x, y, l, r = map(int, input().split())
    result = solve(x,y,l,r)
    print(result)
