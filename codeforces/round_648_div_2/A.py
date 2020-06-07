def solve(matrix):
    r = len(matrix) - sum([1 if sum(row)>0 else 0 for row in matrix ])
    c = len(matrix[0]) - sum([1 if sum([row[i] for row in matrix]) > 0 else 0 for i in range(len(matrix[0]))])
    minrc = min(r, c)
    #print(r, c)
    if minrc % 2:
        return "Ashish"
    return "Vivek"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    ans = solve(matrix)
    print(ans)
