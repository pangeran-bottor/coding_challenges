def solve(plates, P):
    sums = [-1 for i in range(len(plates))]
    maps = {}

    def recur(n, sums):
        if n == P:
            return 0

        s = str("-".join(map(str, sums))) + str(n)
        if s in maps:
            return maps[s]

        max_ = 0
        for i in range(len(sums)):
            sums[i] += 1
            if len(plates[i]) > sums[i]:
                max_ = max(recur(n+1, sums) + plates[i][sums[i]], max_)
            sums[i] -= 1
        maps[s] = max_
        return max_

    result = recur(0, sums)
    return result

T = int(input())
for t in range(T):
    N, K, P = map(int, input().split())
    plates = []
    for _ in range(N):
        plates.append(list(map(int, input().split())))
    result = solve(plates, P)
    print("Case #" + str(t+1) + ": " + str(result))