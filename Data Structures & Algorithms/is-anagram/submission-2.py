class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1
        for c in t:
            if c in counter:
                counter[c] -= 1
                if counter[c] < 1:
                    del counter[c]
        return len(counter) == 0