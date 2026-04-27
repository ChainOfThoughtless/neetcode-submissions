class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        return self.findMatch(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self.findMatch(prefix, False)
        
    def findMatch(self, string: str, exactMatch: bool) -> bool:
        curr = self.root
        for c in string:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word if exactMatch else True
        