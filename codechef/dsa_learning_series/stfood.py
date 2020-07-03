# https://www.codechef.com/LRNDSA02/problems/STFOOD

t = int(input())
for _ in range(t):
    N = int(input())
    ans = 0
    for _ in range(N):
        s, p, v = map(int, input().split())
        ans = max(ans,
            p//(s+1) * v
        )
    print(ans)
