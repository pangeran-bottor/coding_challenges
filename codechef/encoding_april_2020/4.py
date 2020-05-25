def solve(N, K, a):
    extended_a = a + a[:K]
    prefix_sum = [0]
    for el in extended_a:
        prefix_sum.append(prefix_sum[-1] + el)
    
    result = 0
    for i in range(len(prefix_sum)-K):
        result = max(result, prefix_sum[i+K]-prefix_sum[i])
    return result
    

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    result = solve(N, K, a)
    print(result)