class UnionFind:
    def __init__(self, nums):
        self.par = {x: x for x in nums}
        self.rank = {x: 1 for x in nums}
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        if y not in self.par:
            return
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.par[fy] = fx
        self.rank[fx] += self.rank[fy]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        uf = UnionFind(numSet)
        for n in numSet:
            if n + 1 in numSet:
                uf.union(n, n + 1)
        
        return max(uf.rank.values())


