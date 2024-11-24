class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = 0
        n = len(matrix)
        countNegatives = 0
        smallestAbsolute = float('inf')

        for i in range(n):
            for j in range(n):
                sum += abs(matrix[i][j])

                if matrix[i][j] < 0:
                    countNegatives +=1
                smallestAbsolute = min(smallestAbsolute,abs(matrix[i][j]))
        if countNegatives % 2 == 0:
            return sum
        return sum - 2*smallestAbsolute