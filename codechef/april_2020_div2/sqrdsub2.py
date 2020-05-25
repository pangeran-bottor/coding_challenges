from collections import defaultdict


def solve(N, A):

    for i in range(N):
        if A[i] % 4 == 0:
            A[i] = 2
        elif A[i] % 2 == 0:
            A[i] = 1
        else:
            A[i] = 0

    result = 0
    prevsum = defaultdict(lambda: 0)
    currsum = 0

    for i in range(N):
        currsum += A[i]

        if currsum == 1:
            result += 1

        if currsum - 1 in prevsum:
            result += prevsum[currsum - 1]

        prevsum[currsum] += 1
            
    final_result = N*(N+1) // 2 - result 
    return final_result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = solve(N, A)
    print("{}".format(result))