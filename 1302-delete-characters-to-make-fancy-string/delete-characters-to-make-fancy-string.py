class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        res = [s[0]]
        freq = 1
        

        for i in range(1,n):
            if s[i] == res[-1]:
                freq += 1
                if freq<3:
                    res.append(s[i])
            else:
                res.append(s[i])
                freq = 1
        return ''.join(res)

