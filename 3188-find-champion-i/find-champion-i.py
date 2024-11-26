class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            isChamp = True
            for j in range(n):
                if i != j and grid[j][i] == 1:
                    isChamp = False
                    break
            if isChamp:
                return i
        return -1