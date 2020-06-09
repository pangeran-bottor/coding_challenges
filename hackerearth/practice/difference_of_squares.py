# https://www.hackerearth.com/problem/algorithm/difference-of-squares-69d144a5/description/


def solve(L, R):
    def count(n):
        c = 0
        c += n//4
        c += (n+3)//4
        c += (n+1)//4
        return c
    #print(count(R), count(L-1))
    return count(R)-count(L-1)



T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    ans = solve(L, R)
    print(ans)

