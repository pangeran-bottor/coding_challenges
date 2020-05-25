def solve(n, k, arr):
    arr_set_list = list(set(arr))
    #print(arr_set_list)
    if k < len(arr_set_list):
        return "-1"


    while k - len(arr_set_list) > 0:
        for i in range(1, n+1):
            if i not in arr_set_list:
                arr_set_list.append(i)
                break

    arr_set_list.sort()
    #print(arr_set_list)
    result = []
    for _ in range(n):
        result += arr_set_list
    return "{}\n{}".format(len(result), " ".join(map(str, result)))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = solve(n, k, arr)
    print(result)