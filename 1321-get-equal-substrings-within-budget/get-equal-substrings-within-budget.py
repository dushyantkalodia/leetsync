class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        i,j = 0,0
        currCost = 0
        maxLen = 0 

        while j<n:
            currCost += abs(ord(s[j])-ord(t[j]))
            while currCost > maxCost:
                currCost -= abs(ord(s[i]) - ord(t[i]))
                i+=1
            maxLen = max(maxLen,j-i+1)
            j+=1
        return maxLen