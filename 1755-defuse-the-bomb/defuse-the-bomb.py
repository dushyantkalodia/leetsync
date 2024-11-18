class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        if k == 0:
            return [0]*n
        for i in range(n):

            if k<0:
                for j in range(1,-k+1):
                    res[i] += code[(i-j+n)%n]
            else:
                for j in range(1,k+1):
                    res[i] += code[(i+j)%n]
        return res
