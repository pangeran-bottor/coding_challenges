# https://www.codechef.com/LRNDSA02/problems/PSHOT
def solve(N, S):
    c1, s1 = N, 0
    c2, s2 = N, 0
    for i in range(len(S)):
        if i % 2 == 0:
            c1 -= 1
            s1 += int(S[i])
        else:
            c2 -= 1
            s2 += int(S[i])
        
        if s1 > s2 + c2:
            return i+1
        if s2 > s1 + c1:
            return i+1
    return 2*N

t = int(input())
for _ in range(t):
    N = int(input())
    S = input()
    ans = solve(N, S)
    print(ans)