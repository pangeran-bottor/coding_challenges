def normalize(s):
    while "()" in s:
        s = s.replace("()", "")
    return s

n = int(input())
inputs = []
for _ in range(n):
    s = input()
    s = normalize(s)
    if len(s) > 0:
        inputs.append(s)


