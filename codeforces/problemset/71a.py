def solve(word):
    if len(word) > 10:
        return "{}{}{}".format(word[0], str(len(word)-2), word[-1])
    return word


t = int(input())
for _ in range(t):
    word = input()
    result = solve(word)
    print(result)
