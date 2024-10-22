class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfsFill(grid: List[List[str]],i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            grid[i][j] = '0'
            dfsFill(grid,i+1,j)
            dfsFill(grid,i-1,j)
            dfsFill(grid,i,j+1)
            dfsFill(grid,i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfsFill(grid,i,j)
                    count += 1
        return count