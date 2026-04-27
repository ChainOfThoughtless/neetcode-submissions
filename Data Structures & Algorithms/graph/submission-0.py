class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        
        if dst not in self.adjList:
            self.adjList[dst] = set()
        
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False

        def dfs(curr, visited):
            if curr in visited:
                return 0
            if curr == dst:
                return 1
            visited.add(curr)
            path = 0
            for neighbor in self.adjList[curr]:
                path += dfs(neighbor, visited)
            visited.remove(curr)
            return path
        return dfs(src, set()) > 0
