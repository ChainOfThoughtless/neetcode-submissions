class Pair:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.table = [None] * self.cap

    def _hash(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        node = self.table[index]
        if not node: #no collision
            self.table[index] = Pair(key, value)
            self.size += 1
        else: 
            prev = None
            while node:
                if node.key == key: #update only
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Pair(key, value) #open address
            self.size += 1
        # check capacity
        if self.size / self.cap >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        newCap = self.cap * 2
        newTable = [None] * newCap
        for node in self.table:
            while node:
                index = node.key % newCap
                if newTable[index] is None:
                    newTable[index] = Pair(node.key, node.val)
                else:
                    newNode = newTable[index]
                    while newNode.next:
                        newNode = newNode.next
                    newNode.next = Pair(node.key, node.val)
                node = node.next
        self.cap = newCap
        self.table = newTable
