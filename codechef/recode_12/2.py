def solve(S):
    if len(S) <= 2: return "YES"

    L = S[1:] + S[0]
    R = S[-1] + S[:-1]
    if L == R: return "YES"
    return "NO"


T = int(input())
for _ in range(T):
    S = input()
    result = solve(S)
    print(result)