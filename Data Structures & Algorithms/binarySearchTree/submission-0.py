class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)
        if self.root == None:
            self.root = node
            return
        
        current = self.root
        while True:
            if current.key < key:
                if current.right == None:
                    current.right = node
                    return
                current = current.right
            elif current.key > key:
                if current.left == None:
                    current.left = node
                    return
                current = current.left
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        def bst(root, key):
            if root == None:
                return -1
            if root.key > key:
                return bst(root.left, key)
            if root.key < key:
                return bst(root.right, key)
            return root.val
        return bst(self.root, key)

    def getMin(self) -> int:
        curr = self.root
        while curr:
            if curr.left:
                curr = curr.left
            else:
                break
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        def deleteNode(root, key):
            if not root:
                return root
            if root.key > key:
                root.left = deleteNode(root.left, key)
            elif root.key < key:
                root.right = deleteNode(root.right, key)
            else:
                #found node
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                
                # find left most from right
                curr = root.right
                while curr.left:
                    curr = curr.left
                # #swap
                # root.key = curr.key
                # root.val = curr.val
                # root.right = deleteNode(root.right, key)
                #delete
                curr.left = root.left
                res = root.right
                del root
                return res
            return root
        self.root = deleteNode(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.key)
            dfs(root.right, res)
        dfs(self.root, res)
        return res



