def solve(N, a):
    cur = {5:0, 10:0, 15:0}
    for el in a:
        if el == 5:
            cur[5] += 1
        elif el == 10:
            if cur[5] == 0:
                return "NO"
            cur[5] -= 1
            cur[10] += 1
        elif el == 15:
            if cur[10] == 0:
                if cur[5] >= 2:
                    cur[5] -= 2
                else:
                    return "NO"
            else:
                cur[10] -= 1
                cur[15] += 1
    return "YES"


T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    result = solve(N, a)
    print(result)