class Solution:
    def __init__(self):
        self.res = [] 
        self.st = set()
    def solve(self,nums:List[int],temp:List[int],n:int) -> List[List[int]]:
        if len(temp) == n:
            self.res.append(temp[:])
            return

        for i in range(0,n):
            if nums[i] not in self.st:
                temp.append(nums[i]) 
                self.st.add(nums[i]) 
                self.solve(nums,temp,n)
                temp.pop()
                self.st.remove(nums[i])  

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        temp = []
        self.solve(nums,temp,n)
        return self.res