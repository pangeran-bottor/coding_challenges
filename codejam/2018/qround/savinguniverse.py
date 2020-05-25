def solve(D, P):
    def get_damage(plist):
        damage = 0
        hit = 1
        for ch in plist:
            if ch == "S":
                damage += hit
            else:
                hit *= 2
        return damage

    result = 0
    plist = list(P)

    while "CS" in "".join(plist) and get_damage(plist) > D:
        for i in range(len(P)-1, 0, -1):
            if plist[i-1] == "C" and plist[i] == "S":
                plist[i-1], plist[i] = "S", "C"
                result += 1
                break

    if get_damage(plist) <= D:
        return result
    return "IMPOSSIBLE"

T = int(input())
for tc in range(1, T+1):
    input_str = input()
    D, P = int(input_str.split()[0]), input_str.split()[1]
    result = solve(D, P)
    print("Case #{}: {}".format(tc, result))