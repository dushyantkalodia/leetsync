class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        maxRows = 0
        for currRow in matrix:
            inverted = list(range(n-1,-1,-1))
            for col in range(n):
                inverted = [1 if currRow[col] == 0 else 0 for col in range(m)]
            count = 0
            for row in matrix:
                if row == currRow or row == inverted:
                    count += 1
            maxRows = max(maxRows,count)
        return maxRows