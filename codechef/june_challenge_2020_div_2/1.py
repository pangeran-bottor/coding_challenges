def solve(N, K, P):
    ans = 0
    for p in P:
        if p > K:
            ans += (p-K)
    return ans


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    result = solve(N, K, P)
    print(result)