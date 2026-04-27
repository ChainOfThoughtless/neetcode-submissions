class Node:
    def __init__(self, val: int):
        self.value = val
        self.right = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        node = self.head
        itrIdx = 0
        while node and itrIdx < index:
            node = node.right
            itrIdx += 1
        #found the node
        return node.value

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.right = self.head
            self.head = node
        self.length += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.right = node
            self.tail = node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        node = prev= self.head
        itrIdx = 0
        while itrIdx < index:
            prev = node
            node = node.right
            itrIdx += 1
        #found the node
        if node == self.head:
            self.head = node.right
        elif node == self.tail:
            prev.right = None
            self.tail = prev
        else:
            prev.right = node.right
        del node
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        node = self.head
        while node:
            res.append(node.value)
            node = node.right
        return res
