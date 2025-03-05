class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        gola = -1

        for i in range(n-2, -1, -1):  # Iterate from second last element to start
            if nums[i] < nums[i+1]:  # First smaller element
                gola = i
                break
        
        if gola != -1:
            for j in range(n-1, gola, -1):  # Iterate from the end
                if nums[j] > nums[gola]:  # First element greater than nums[gola]
                    nums[gola], nums[j] = nums[j], nums[gola]  # Swap
                    break

        nums[gola+1:] = reversed(nums[gola+1:])