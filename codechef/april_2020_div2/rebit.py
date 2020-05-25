import math


mapper =  {'0&0': '0',  
 '0&1': '0',  
 '1&0': '0',  
 '1&1': '1',  
 '0|0': '0',  
 '0|1': '1',  
 '1|0': '1',  
 '1|1': '1',  
 '0^0': '0',  
 '0^1': '1',  
 '1^0': '1',  
 '1^1': '0',  
 'a&1': 'a',
 '1&a': 'a',
 'a&0': '0',
 '0&a': '0',
 'a&A': '0',
 'A&a': '0',
 'a&a': 'a',
 'A&1': 'A',
 '1&A': 'A',
 'A&0': '0',
 '0&A': '0',
 'A&A': 'A',
 'a|1': '1',
 '1|a': '1',
 'a|0': 'a',
 '0|a': 'a',
 'a|A': '1',
 'A|a': '1',
 'a|a': 'a',
 'A|1': '1',
 '1|A': '1',
 'A|0': 'A',
 '0|A': 'A',
 'A|A': 'A',
 'a^1': 'A',
 '1^a': 'A',
 'a^0': 'a',
 '0^a': 'a',
 'a^A': '1',
 'A^a': '1',
 'a^a': '0',
 'A^1': 'a',
 '1^A': 'a',
 'A^0': 'A',
 '0^A': 'A',
 'A^A': '0'}
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

    found_first = False
    last_op = None
    past_possibility = None
    for l in L:
        if l in ("&", "|", "^"):
            if not found_first:
                for ch in resultmap:
                    resultmap[ch] *= multiplier[l][ch]
                found_first = True
                last_op = l
            else:
                past_possibility = 
                tmp_map = dict(resultmap)
                for key in resultmap:
                    resultmap[key] = 0
                for i in ("0", "1", "a", "A"):
                    for j in ("0", "1", "a", "A"):
                        exp = i + l + j
                        expresult = mapper[exp]

                        resultmap[expresult] += tmp_map[i]
                        

    el1 = fmod(resultmap["0"], total_expressions)
    el2 = fmod(resultmap["1"], total_expressions)
    el3 = fmod(resultmap["a"], total_expressions)
    el4 = fmod(resultmap["A"], total_expressions)
    print(resultmap, total_expressions)
    return " ".join(map(str, [el1, el2, el3, el4]))

T = int(input())
for tc in range(1, T+1):
    L = input()
    L = L.replace("(", "")
    L = L.replace(")", "")
    result = solve(L)
    print(result)
