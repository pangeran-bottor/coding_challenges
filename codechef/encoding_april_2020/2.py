def solve(N, s):
    s = list(s)
    s.sort()
    return s[0]

T = int(input())
for _ in range(T):
    N = int(input())
    s = input()
    result = solve(N, s)
    print(result)