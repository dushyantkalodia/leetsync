class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        top = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                if count>top:
                    top = count
                count = 0
        if count>top:
            top = count
        return top