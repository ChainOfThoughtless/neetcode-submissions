class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, node): # to head
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.size += 1
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeTail(self):
        if self.size > 0:
            lruNode = self.tail.prev
            self.removeNode(lruNode)
            return lruNode
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node
        self.freq_map = {} # freq -> DLinkedList
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.updateFreq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return 

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.updateFreq(node)
            return

        # add new, cap check first to evict
        if len(self.cache) >= self.cap:
            lfuNode = self.freq_map[self.min_freq].removeTail()
            if lfuNode:
                del self.cache[lfuNode.key] 
        
        # add new
        node = Node(key, value)
        self.cache[key] = node
        self.min_freq = 1
        if self.min_freq not in self.freq_map:
            self.freq_map[self.min_freq] = DLinkedList()
        self.freq_map[self.min_freq].addNode(node)
        
    def updateFreq(self, node):
        # remove ndoe from current freq map
        freq = node.freq
        self.freq_map[freq].removeNode(node)
        
        # update min freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq = freq + 1

        # insert to new freq map
        freq += 1
        node.freq += 1
        if freq not in self.freq_map:
            self.freq_map[freq] = DLinkedList()
        self.freq_map[freq].addNode(node)
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)