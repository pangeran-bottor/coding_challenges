def solve(N, matrix):
    k, r, c = 0, 0, 0

    for i in range(N):
        k += matrix[i][i]

    for row in matrix:
        if len(set(row)) != N:
            r += 1
    
    for i in range(N):
        if len(set([row[i] for row in matrix])) != N:
            c += 1
    return " ".join(map(str, [k, r, c]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    result = solve(N, matrix)
    print("Case #{}: {}".format(tc, result))