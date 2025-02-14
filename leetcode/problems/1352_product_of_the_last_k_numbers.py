class ProductOfNumbers:
    def __init__(self):
        self.mem = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.mem = [1]
        else:
            self.mem.append(num * self.mem[-1])

    def getProduct(self, k: int) -> int:
        if k > len(self.mem) - 1:
            return 0
        return self.mem[-1] // self.mem[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
