# https://www.codechef.com/LRNDSA02/problems/STUPMACH

def solve(N, S):
    ans = 0
    cur_min = S[0]
    for i in range(N):
        cur_min = min(cur_min, S[i])
        ans += cur_min
    return ans


t = int(input())
for _ in range(t):
    N = int(input())
    S = list(map(int, input().split()))
    ans = solve(N, S)
    print(ans)