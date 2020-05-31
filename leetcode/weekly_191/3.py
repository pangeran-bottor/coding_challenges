# https://leetcode.com/contest/weekly-contest-191/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

def minReorder(n, connections):
    result = 0
    direct = {}
    nondirect = []
    for start, to in connections:
        if start == 0:
            direct[to] = start
            result += 1
        elif to == 0:
            direct[start] = to
        else:
            nondirect.append([start, to])
            
    nondirect.sort()
    for start, to in nondirect:
        if start in direct:
            result += 1
            direct[to] = start
        elif to in direct:
            if start not in direct:
                direct[start] = to
    return result
