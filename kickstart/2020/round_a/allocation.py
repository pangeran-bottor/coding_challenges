def solve(N, B, A):
    A.sort()
    
    count = 0
    i = 0 
    while i < N:
        if A[i] <= B:
            B -= A[i]
            count += 1
            i += 1
        else:
            break
    return count
T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    result = solve(N, B, A)
    print("Case #" + str(t+1) + ": " + str(result))
    
    
    