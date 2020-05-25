def solve(N, K):
    MOD = 10**9 + 7
    if K%2==0:
        return ((N+K//2)*(N+K//2-1) + N) %  MOD
    return ((N+(K+1)//2)*(N+(K+1)//2-1)-N) % MOD


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    result = solve(N, K)
    print(result)