class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        summ = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                curr+= nums[i]
            else:
                curr = nums[i]
            summ = max(summ,curr)
        return summ