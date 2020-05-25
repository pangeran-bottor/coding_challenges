def solve(n, a):
    p = a[0][0]
    c = a[0][1]

    for el in a:
        if el[0] < p or el[1] < c:
            return "NO"
        if el[0] < el[1]:
            return "NO"
        if el[0] - p < el[1]-c:
            return "NO"
        p = el[0]
        c = el[1]

    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list()
    for _ in range(n):
        a.append(list(map(int, input().split())))
    result = solve(n, a)
    print(result)