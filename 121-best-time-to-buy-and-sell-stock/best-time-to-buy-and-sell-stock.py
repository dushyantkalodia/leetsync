class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxp = 0

        for i in prices:
            if i < minp:
                minp = i
            profit = i - minp

            if profit > maxp:
                maxp = profit

        return maxp