class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        def markGuarded(row,col,grid):
            
            for i in range(row-1,-1,-1):
                if grid[i][col] == 2 or grid[i][col] == 3:
                    break
                grid[i][col] = 1
          
            for i in range(row+1,len(grid)):
                if grid[i][col] == 2 or grid[i][col] == 3:
                    break
                grid[i][col] = 1
            
            for i in range(col-1,-1,-1):
                if grid[row][i] == 2 or grid[row][i] == 3:
                    break
                grid[row][i] = 1
            
            for i in range(col+1,len(grid[0])):
                if grid[row][i] == 2 or grid[row][i] == 3:
                    break
                grid[row][i] = 1

        for vec in guards:
            i = vec[0]
            j = vec[1]
            grid[i][j] = 2
        for vec in walls:
            i = vec[0]
            j = vec[1]
            grid[i][j] = 3
        for guard in guards:
            i = guard[0]
            j = guard[1]
            markGuarded(i,j,grid)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count