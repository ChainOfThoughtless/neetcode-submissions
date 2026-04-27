class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i] if i < self.length else None


    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.arr[i] = n
            

    def pushback(self, n: int) -> None:
        if self.length < self.capacity:
            self.arr[self.length] = n
            self.length += 1
        else:
            self.resize()
            self.pushback(n)

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
            return self.arr[self.length]

 

    def resize(self) -> None:
        newArr = [0] * self.capacity
        self.arr += newArr
        self.capacity *= 2


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity