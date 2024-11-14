class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankset = set(bank)
        visited = set([startGene])
        q = deque([startGene])
        
        level = 0

        while q:
            n = len(q)
            while n > 0:
                n -= 1
                cur = q.popleft()
                if cur == endGene:
                    return level
                for ch in "ACGT":
                    for i in range(len(cur)):
                        neighbor = cur[:i] + ch + cur[i+1:]


                        if neighbor not in visited and neighbor in bankset:
                            visited.add(neighbor)
                            q.append(neighbor)
            level+=1    
        return  -1


