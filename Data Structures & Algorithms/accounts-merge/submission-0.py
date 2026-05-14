class UnionFind:
    def __init__(self, n):
        self.par = {x: x for x in range(n)}
        self.rank = {x: 1 for x in range(n)}
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[self.par[x]])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.par[py] = px
        self.rank[px] += self.rank[py]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        email2Acct = {}
        for i, account in enumerate(accounts):
            for e in account[1:]:
                if e not in email2Acct:
                    email2Acct[e] = i
                else:
                    uf.union(i, email2Acct[e])
        
        emailGroup = defaultdict(list)
        for e, i in email2Acct.items():
            lead = uf.find(i)
            emailGroup[lead].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res










