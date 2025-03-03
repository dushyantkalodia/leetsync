class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        lesspivot = []
        equalpivot = []
        morepivot = []

        for i in range(n):
            if nums[i]< pivot:
                lesspivot.append(nums[i])
            elif nums[i] == pivot:
                equalpivot.append(nums[i])
            else:
                morepivot.append(nums[i])
        
        for num in equalpivot:
            lesspivot.append(num)
        
        for num in morepivot:
            lesspivot.append(num)
        return lesspivot