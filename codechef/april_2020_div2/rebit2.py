import math

multiplier = {'&': {'0': 9, '1': 1, 'a': 3, 'A': 3},
                '|': {'0': 1, '1': 9, 'a': 3, 'A': 3},
                '^': {'0': 4, '1': 4, 'a': 4, 'A': 4}}
M = 998244353
def modexp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modexp((x*x)%M, n//2)
    else:
        return (x*modexp((x*x)%M, (n-1)/2)%M)

def fmod(a, b):
    c = math.gcd(a, b)
    a = a//c 
    b = b//c
    d = modexp(b, M-2)
    ans = ((a % M) * (d % M)) % M 
    return ans

def solve(L):
    resultmap = {
        "0": 1, "1": 1, "a": 1, "A": 1
    }

    if L == "#":
        el1 = fmod(1, 4)
        return " ".join(map(str, [el1, el1, el1, el1]))

    total_expressions = 1
    for l in L:
        if l == "#":
            total_expressions *= 4

        if l in multiplier:
            for ch in resultmap:
                resultmap[ch] *= multiplier[l][ch]
    
    el1 = fmod(resultmap["0"], total_expressions)
    el2 = fmod(resultmap["1"], total_expressions)
    el3 = fmod(resultmap["a"], total_expressions)
    el4 = fmod(resultmap["A"], total_expressions)
    print(resultmap, total_expressions)
    return " ".join(map(str, [el1, el2, el3, el4]))

T = int(input())
for tc in range(1, T+1):
    L = input()
    result = solve(L)
    print(result)