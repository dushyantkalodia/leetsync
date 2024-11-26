class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        indx = 0
        m = grid[0]
        for i in range(len(grid)):
            if sum(grid[i])> sum(m):
                m = grid[i]
                indx = i
        return indx