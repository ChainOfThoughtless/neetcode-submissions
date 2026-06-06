class Solution:

    def encode(self, strs: List[str]) -> str:
        # length-prefix
        string = ''
        for s in strs:
            string += str(len(s)) + '#' + s
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        l = 0
        r = l
        while r < len(s):
            if s[r] != '#':
                r += 1
                continue
            length = int(s[l:r])
            strs.append(s[r + 1 : r + 1 + length])
            l = r + 1 + length
            r = l
        return strs