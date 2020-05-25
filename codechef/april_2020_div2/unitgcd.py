import math


def solve(N):
    if N <= 3:
        return [[i for i in range(1, N+1)]]

    result = [[1, 2, 3]]
    for i in range(4, N+1):
        if len(result[-1]) >= 2:
            result.append([i])
        else:
            result[-1].append(i)
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = solve(N)
    print(len(result))
    for r in result:
        print(str(len(r)) + " " + " ".join(map(str, r)))
