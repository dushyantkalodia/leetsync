class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)

        for i in range(n):
            summ+=nums[i]
        ans = (n*(n+1))//2 - summ

        return ans