T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    S = input()
    counter = {}
    for s in S:
        if s not in counter:
            counter[s] = 0
        counter[s] += 1
    for _ in range(Q):
        result = 0
        C = int(input())
        for c in counter:
            if counter[c] - C > 0:
                result += counter[c]-C
        print(result)