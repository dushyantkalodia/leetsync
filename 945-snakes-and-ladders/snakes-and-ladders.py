class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        steps = 0
        q = deque([1])
        visited = [[False] * n for _ in range(n)]
        visited[n-1][0] = True
        def getCoord(val):
            rowT = (val-1)//n
            rowB = (n-1) - rowT

            col = (val-1)%n
            if (n%2 == 1 and rowB%2 == 1) or (n%2 == 0 and rowB%2 == 0):
                col = (n-1) - col
            return (rowB,col)

        
        while q:
            N = len(q)
            while N>0:
                N -= 1
                x = q.popleft()
                if x == n*n:
                    return steps
                for k in range(1,7):
                    val = x+k
                    if val > n*n:
                        break
                    coord = getCoord(val)
                    r, c = coord
                    if visited[r][c] == True:
                        continue
                    visited[r][c] = True
                    if board[r][c] == -1:
                        q.append(val)
                    else:
                        q.append(board[r][c])
            steps += 1
        return -1

