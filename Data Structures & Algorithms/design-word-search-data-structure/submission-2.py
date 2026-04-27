class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        return self.findStr(word, self.root)
        
    def findStr(self, word, node):
        if not word:
            return node.word
        c = word[0]
        if c == '.':
            for child in node.children:
                if self.findStr(word[1:], node.children[child]):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self.findStr(word[1:], node.children[c])
