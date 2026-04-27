class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.size = k
        for num in nums:
            self.push(num)

    def push(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
        if len(self.heap) - 1 > self.size:
            self.pop()
    
    def pop(self):
        if len(self.heap) <= 1:
            return
        if len(self.heap) == 2:
            self.heap.pop()
            return
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            #swap with right child
            if (2 * i + 1 < len(self.heap)) and \
            self.heap[i] > self.heap[2 * i + 1] and \
            self.heap[2 * i + 1] < self.heap[2 * i]:
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break

    def add(self, val: int) -> int:
        self.push(val)
        return self.heap[1]
