def solve(N, M, K, tups):
    if M == 1:
        result = [tup[0] for tup in tups]
        return " ".join(map(str, result))
    if M == 2:
        result = []
        for tup in tups:
            tupset = set([el for el in tup])
            if len(tupset) == 1:
                result.append(tup[0])
            else:
                result.append(1)
        return " ".join(map(str, result))
    
    result = []
    for tup in tups:
        tupset = set([el for el in tup])
        result.append(tup[0])
    return " ".join(map(str, result))

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    tups = []
    for _ in range(N):
        tup = tuple(map(int, input().split()))
        tups.append(tup)
    result = solve(N, M, K, tups)
    print("{}".format(result))