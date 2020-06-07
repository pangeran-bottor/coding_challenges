# https://www.codechef.com/LRNDSA07/problems/SUBINC


def solve(arr):
    nondec = []
    for el in arr:
        if not nondec:
            nondec.append([el])
        else:
            if el >= nondec[-1][-1]:
                nondec[-1].append(el)
            else:
                nondec.append([el])
    ans = 0
    for dec in nondec:
        ndec = len(dec)
        ans += (ndec * (ndec+1))//2
    return ans
    
    
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = solve(arr)
    print(ans)

