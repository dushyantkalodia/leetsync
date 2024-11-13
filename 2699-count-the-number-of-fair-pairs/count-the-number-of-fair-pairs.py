class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  # Sorts the list in-place, O(n log n)
        n = len(nums)
        result = 0

        for i in range(n):
        # Find the first position where (lower - nums[i]) can be inserted to keep sorted order
            idx_lower = bisect_left(nums, lower - nums[i], i + 1, n)
            
            # Find the first position where (upper - nums[i]) is greater
            idx_upper = bisect_right(nums, upper - nums[i], i + 1, n)
            
            # Count of elements in the range
            result += (idx_upper - idx_lower)
        
        return result