class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(row,col,direction):
            dr,dc = direction
            r,c = row+dr,col+dc
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] == 2 or grid[r][c] == 3:
                    break
                if grid[r][c] == 0:
                    grid[r][c] = 1
                r+=dr
                c+=dc


        for i,j in guards:
            grid[i][j] = 2
        for i,j in walls:
            grid[i][j] = 3
        for i,j in guards:
            for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(i,j,direction)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count