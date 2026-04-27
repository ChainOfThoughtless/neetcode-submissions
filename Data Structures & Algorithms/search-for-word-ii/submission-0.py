class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.insert(word)

        res = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r, c, node, word, visited):
            if (r < 0 or c < 0 or r >= ROW or \
                c >= COL or (r, c) in visited or \
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word, visited)
            dfs(r - 1, c, node, word, visited)
            dfs(r, c + 1, node, word, visited)
            dfs(r, c - 1, node, word, visited)
            visited.remove((r, c))

        #board iterator
        for r in range(ROW):
            for c in range(COL):
                #dfs
                dfs(r, c, root.root, "", set())

        return list(res)
    







        