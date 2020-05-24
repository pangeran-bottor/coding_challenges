# https://codeforces.com/contest/1360/problem/D

def solve(n, k):
    def is_prime(num):
        if num == 1:
            return False
        i = 2
        while i*i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def max_div(num, k):
        divisors = [1, num]
        i = 2
        while i*i <= num:
            if num % i == 0:
                divisors.append(i)
                divisors.append(num//i)
            i += 1
        divisors.sort()

        maxdiv = 1
        for d in divisors:
            if d <= k:
                maxdiv = max(maxdiv, d)
        return num // maxdiv


    if n > k:
        if is_prime(n):
            return n
        else:
            return max_div(n, k)
    return 1


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = solve(n, k)
    print(result)
