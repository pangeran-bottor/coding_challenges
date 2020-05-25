def solve(X, K):
    def prime_factors(n):
        i = 2
        factors = {}
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                if i not in factors:
                    factors[i] = 0
                factors[i] += 1
        if n > 1:
            if n not in factors:
                factors[n] = 0
            factors[n] += 1
        return factors

    pfactors = prime_factors(X)
    slots = sum([pfactors[key] for key in pfactors])
    if slots >= K:
        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    X, K = map(int, input().split())
    result = solve(X, K)
    print("{}".format(result))