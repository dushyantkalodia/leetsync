class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        duplicate = -1
        missing = (n*n)*(1+n*n)//2
        seen = set()
        
        for row in grid:
            for num in row:
                if num not in seen:
                    seen.add(num)
                    missing -= num
                else:
                    duplicate = num
        return [duplicate,missing]