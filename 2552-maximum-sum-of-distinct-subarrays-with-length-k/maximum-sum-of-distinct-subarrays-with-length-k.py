class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        res = 0
        st = set()
        summ = 0
        while j<n:
            while nums[j] in st:
                summ -= nums[i]
                st.remove(nums[i])
                i += 1
            summ += nums[j]
            st.add(nums[j])

            if j-i+1 == k:
                res = max(res,summ)
                summ -= nums[i]
                st.remove(nums[i])
                i += 1
            j += 1
        return res

