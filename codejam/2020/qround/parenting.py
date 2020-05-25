def solve(N, A):
    atups = []
    for a in A:
        atups.append((a[0], a[1]))
    db = {}

    end = [['C', None], ['J', None]]

    A.sort()
    end = [['C', A[0][1]], ['J', A[1][1]]]
    tup1 = (A[0][0], A[0][1])
    tup2 = (A[1][0], A[1][1])
    if tup1 == tup2:
        db[tup1] = ['C', 'J']
    else:
        db[tup1] = ['C']
        db[tup2] = ['J']

    for a in A[2:]:
        tup = (a[0], a[1])
        s = a[0]
        e = a[1]

        end.sort(key=lambda x: x[1])
        if s < end[0][1]:
            return "IMPOSSIBLE"
        else:
            end[0][1] = e
            if tup not in db:
                db[tup] = []
            db[tup].append(end[0][0])

    result = []
    for a in atups:
        tup = (a[0], a[1])
        cand = db[tup].pop(0)
        result.append(cand)

    return "".join(result)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    result = solve(N, A)
    print("Case #{}: {}".format(tc, result))