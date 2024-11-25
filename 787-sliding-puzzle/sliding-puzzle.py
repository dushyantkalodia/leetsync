class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ""
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])
        target = "123450"
        q = deque([start])
        mp = {}
        mp[0] = {1,3}
        mp[1] = {0,2,4}
        mp[2] = {1,5}
        mp[3] = {0,4}
        mp[4] = {1,3,5}
        mp[5] = {2,4}

        visited = set(start)
        level = 0
        while q:
            n = len(q)
            while n>0:
                n-=1
                curr = q.popleft()
                if curr == target:
                    return level
                indexOfZero = curr.find('0')
                for swapIdx in mp[indexOfZero]:
                    newState = list(curr)
                    newState[indexOfZero], newState[swapIdx] = newState[swapIdx], newState[indexOfZero]
                    newState = ''.join(newState)
                    if newState not in visited:
                        q.append(newState)
                        visited.add(newState)
            level += 1
        return -1