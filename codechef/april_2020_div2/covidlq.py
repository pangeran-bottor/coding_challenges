def solve(N, A):
    latest = None
    for i in range(N):
        if A[i] == 1:
            if latest is None:
                latest = i
            else:
                if i - latest < 6:
                    return "NO"
                latest = i

    return "YES"

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = solve(N, A)
    print("{}".format(result))