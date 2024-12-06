class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        summ = 0
        st = set(banned)

        for num in range(1,n+1):
            if num in st:
                continue
            if summ + num <= maxSum:
                count+=1
                summ+=num
            else:
                break
        return count