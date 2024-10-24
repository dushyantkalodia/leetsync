class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        def topologicalsort(adj,n,indegree):
            q = deque()
            count = 0

            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
            while q:
                u = q.popleft()
                count += 1
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            if count == n:
                return True
            return False       

        for vec in prerequisites:
            a = vec[0]
            b = vec[1]

            adj[b].append(a)
            indegree[a] += 1
        return topologicalsort(adj,numCourses,indegree)