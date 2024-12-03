class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m = len(s)
        n = len(spaces)

        res = ""

        j = 0
        for i in range(m):
            if j<n and i == spaces[j]:
                res += " "
                j += 1
            res += s[i]
        return res