def solve(N, a):
    mapper = {}
    for el in a:
        if el not in mapper:
            mapper[el] = 0
        mapper[el] += 1
    
    keys = [key for key in mapper]
    keys.sort()
    for key in keys:
        print("{}:{}".format(key, mapper[key]))
    

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    solve(N, a)