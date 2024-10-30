class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        
        if(len(t)>n):
            return ""
        
        mp = {ch: 0 for ch in t}
        for ch in t:
            mp[ch] += 1

        requiredCount = len(t)
        i,j = 0,0

        minWindowSize = float('inf')
        start_i = 0

        while j<n:
            ch = s[j]
            if ch in mp:
                if mp[ch]>0:
                    requiredCount -= 1
                mp[ch] -= 1
            while requiredCount == 0:
                currWindowSize = j-i+1
                if(minWindowSize>currWindowSize):
                    minWindowSize = currWindowSize
                    start_i = i
                if s[i] in mp:
                    mp[s[i]] += 1
                    if mp[s[i]]>0:
                        requiredCount += 1
                i += 1
            j += 1
        if minWindowSize == float('inf'):
            return ""
        else:
            return s[start_i:start_i+minWindowSize]