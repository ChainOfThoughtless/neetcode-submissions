class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.sift_down(1)
        return res

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self.sift_down(i)

    def sift_down(self, i):
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and \
            self.heap[i] > self.heap[i * 2 + 1] and \
            self.heap[i * 2] > self.heap[i * 2 + 1]:
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            else:
                break

    def sift_up(self, idx):
        parent = idx // 2
        while idx > 1 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = idx // 2
        
        