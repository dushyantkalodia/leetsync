class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1 = None
        count1 = 0
        maj2 = None
        count2 = 0

        
        for i in range(len(nums)):
            if nums[i] == maj1:
                count1 += 1
            elif nums[i] == maj2:
                count2 += 1
            elif count1 == 0:
                maj1 = nums[i]
                count1 += 1
            elif count2 == 0:
                maj2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1,count2 = 0,0
        for num in nums:
            if num == maj1:
                count1 += 1
            if num == maj2:
                count2 += 1

        res = []
        n = len(nums)
        if count1 > n//3:
            res.append(maj1)
        if count2 > n//3:
            res.append(maj2)
        
        return res
        