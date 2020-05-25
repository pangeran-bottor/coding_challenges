def solve(s):
    result = 0
    
    cur_char = "X"
    cur_count = 0
    for ch in s:
        if ch == cur_char:
            cur_count += 1
        else:
            result = max(result, cur_count)
            cur_count = 1
            cur_char = ch
    return max(result, cur_count)


s = input()
result = solve(s)
print(result)