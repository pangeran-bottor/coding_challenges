def solve(N, a):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                for el in [[-1,0], [1,0], [0, -1], [0,1]]:
                    ni = i+ el[0]
                    nj = j+el[1]
                    if ni<0 or ni>=N or nj<=0 or nj>=N:
                        continue
                    if a[ni][nj] == 1:
                        return "UNSAFE"
                    #print(i, j, ni, nj)
    return "SAFE"


T = int(input())
for _ in range(T):
    N = int(input())
    a = []
    for _ in range(N):
        a.append(list(map(int, input().split())))
    result = solve(N, a)
    print(result)