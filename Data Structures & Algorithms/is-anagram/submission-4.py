class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
        for i in range(len(s)):
            if t[i] not in count_s or count_s[t[i]] <= 0:
                return False
            count_s[t[i]] -= 1
        return True