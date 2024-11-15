class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        j = n-1

        while j>0 and arr[j] >= arr[j-1]:
            j -= 1

        i = 0
        res = j



        while i<j and (i == 0 or arr[i] >= arr[i-1]):
            while j<n and arr[i] > arr[j]:
                j += 1
            res = min(res,j-i-1)
            i += 1
        return res
