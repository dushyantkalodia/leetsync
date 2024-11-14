class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def wordMatch(cur,mp,q,visited):
            for i in range(len(cur)):

                for c in 'abcdefghijklmnopqrstuvwxyz':
                    s = cur[:i] + c + cur[i+1:]
                    if s in mp and s not in visited:
                        visited.add(s)
                        q.append(s)
                        

        mp = set(wordList)
        q = deque([beginWord])
        visited = set([beginWord])
        level = 1

        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur == endWord:
                    return level
                wordMatch(cur,mp,q,visited)
            level += 1
        return 0