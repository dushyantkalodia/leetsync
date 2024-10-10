class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)

        maxchar = ' '
        for i in range(n):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                maxchar = max(maxchar,num[i])

        if maxchar == ' ':
            return ""

        return maxchar * 3