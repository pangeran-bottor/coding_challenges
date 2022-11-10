class StockSpanner:

    def __init__(self):
        self.stack = [] # (price, index)
        self.index = 0
        

    def next(self, price: int) -> int:
        # price >= self.stack[-1][0] because we need to replace the previous 'blocker'
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        
        self.index += 1
        self.stack.append((price, self.index))
        
        if len(self.stack) == 1:
            return self.index
        
        return self.stack[-1][1] - self.stack[-2][1]
