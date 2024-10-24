class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj = defaultdict(list)

        def dfs(adj,src,dst,visited,product):
            if src in visited:
                return -1.0
            visited.add(src)
            if src == dst:
                return product
                  
            for v,val in adj[src]:
                res = dfs(adj,v,dst,visited,product*val)
                if res != -1.0:
                    return res
            visited.remove(src)
            return -1.0

        for i in range(n):
            u = equations[i][0]
            v = equations[i][1]
            val = values[i]

            adj[u].append((v,val))
            adj[v].append((u,1.0/val))
        
        res = []
        for query in queries:
            src = query[0]
            dst = query[1]

            if src in adj and dst in adj:
                visited = set()
                ans = dfs(adj,src,dst,visited,1.0)
            else:
                ans = -1.0
            res.append(ans)
        return res
