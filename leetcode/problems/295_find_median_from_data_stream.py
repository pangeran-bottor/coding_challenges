from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.low = [] # max-heap
        self.high = [] # min_heap
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count == 0 or self.high[0] > num:
            heappush(self.low, -num)
            if self.count % 2 == 0:
                heappush(self.high, -heappop(self.low))
        else:
            heappush(self.high, num)
            if self.count % 2 == 1:
                heappush(self.low, -heappop(self.high))
        
        self.count += 1
        

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.high[0] - self.low[0]) / 2
        return self.high[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
