def solve(S):
    def get_groups(S):
        groups = []
        cur_str = None
        for s in S:
            if not cur_str:
                cur_str = s
            elif s == cur_str[-1]:
                cur_str += s
            else:
                groups.append(cur_str)
                cur_str = s
        groups.append(cur_str)
        return groups

    groups = get_groups(S)
    #print(groups)
    stack = []
    tmp = []
    #cur_group = None

    for group in groups:
        num = int(group[0])
        if num == 0:
            stack.append(group)
            continue

        if not stack:
            for _ in range(num):
                stack.append("(")
            stack.append(group)
            for _ in range(num):
                stack.append(")")
        else:
            while stack[-1] == ")":
                tmp.append(stack.pop())
            #print(tmp)

            if num > len(tmp):
                for _ in range(num - len(tmp)):
                    stack.append("(")
                stack.append(group)
                for _ in range(num-len(tmp)):
                    stack.append(")")
                while tmp:
                    stack.append(tmp.pop())
            else:
                for _ in range(len(tmp)-num):
                    stack.append(tmp.pop())
                stack.append(group)
                while tmp:
                    stack.append(tmp.pop())
        #print("".join(stack))
    result = "".join(stack)
    return result

T = int(input())
for tc in range(1, T+1):
    S = input()
    result = solve(S)
    print("Case #{}: {}".format(tc, result))