def solve(N, P):
    P.sort()
    m = 10**9 + 7
    for i in range(N):
        P[i] -= (N-1-i)
    
    result = 0
    for p in P:
        if p > 0:
            result += p
            result %= m
    
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    result = solve(N, P)
    print("{}".format(result))