import heapq


class NumberContainers:
    def __init__(self):
        self.current = {}
        self.heap_map = {}

    def change(self, index: int, number: int) -> None:
        if self.current.get(index, -1) == number:
            return

        self.current[index] = number
        if number not in self.heap_map:
            self.heap_map[number] = []
        heapq.heappush(self.heap_map[number], index)

    def find(self, number: int) -> int:
        if number not in self.heap_map:
            return -1

        while self.heap_map[number]:
            index = self.heap_map[number][0]
            if self.current.get(index) == number:
                return index

            heapq.heappop(self.heap_map[number])
        return -1
