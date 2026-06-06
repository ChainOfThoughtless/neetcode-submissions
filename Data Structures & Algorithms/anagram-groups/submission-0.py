class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []
        for s in strs:
            k = tuple(sorted(s))
            if k not in hm:
                hm[k] = []
            hm[k].append(s)
        return list(hm.values())