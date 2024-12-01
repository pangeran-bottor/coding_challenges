class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        div = (money - children) // 7
        rem = (money - children) % 7

        if children < div:
            return children - 1
        elif children == div and rem > 0:
            return children - 1
        elif children == div and rem == 0:
            return children
        elif children == div + 1 and rem == 3:
            return max(0, div - 1)
        return div
