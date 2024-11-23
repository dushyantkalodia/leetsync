class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [['' for _ in range(m)] for _ in range(n)]
        #transpose the matrix
        for i in range(n):
            for j in range(m):
                res[i][j] = box[j][i]
        #reverse each row 
        for row in res:
            row.reverse()
        #adjust stones based on gravity
        for j in range(m):
            for i in range(n-1,-1,-1):
                if res[i][j] == '.':
                    stoneRow = -1
                    for k in range(i-1,-1,-1):
                        if res[k][j] == '*':
                            break
                        elif res[k][j] == '#':
                            stoneRow = k
                            break
                    if stoneRow != -1:
                        res[i][j] = '#'
                        res[stoneRow][j] = '.'
        return res