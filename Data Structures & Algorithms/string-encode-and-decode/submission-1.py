class Solution:

    def encode(self, strs: List[str]) -> str:
        # length-prefix
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            strs.append(s[j + 1 : 
            j + 1 + length])
            i = j + 1 + length
        return strs