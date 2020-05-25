def solve(N, X):
    count = 0
    N.sort(reverse=True)

    idx = 0
    while X > 0 and idx < len(N):
        if N[idx] == X:
            count += 1
            return count
        elif N[idx] > X:
            idx += 1
        else:
            X -= N[idx]
            count += 1
    return count


T = int(input())
for _ in range(T):
    N = list(map(int, input().split()))
    X = int(input())
    result = solve(N, X)
    print(result)