def solve(R, C, x, y):
    # c1 = (x+1) + (C-y) - 2 # to top right
    # c2 = (R-x) + (C-y) - 2 # to bottom right
    # c3 = (R-x) + (y+1) - 2 # to bottom left
    # c4 = (x+1) + (y+1) - 2 # to top left
    c1 = max(x+1, C-y)-1
    c2 = max(R-x, C-y)-1
    c3 = max(R-x, y+1)-1
    c4 = max(x+1, y+1)-1
    result = max([c1, c2, c3, c4])
    return result


T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    x, y = map(int, input().split())
    result = solve(R, C, x, y)
    print(result)