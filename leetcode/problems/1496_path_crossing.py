class Solution:
    def isPathCrossing(self, path: str) -> bool:
        MOVES = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

        visited = set()
        cur = (0, 0)

        visited.add(cur)
        for p in path:
            cur = (cur[0] + MOVES[p][0], cur[1] + MOVES[p][1])
            if cur in visited:
                return True
            visited.add(cur)

        return False
