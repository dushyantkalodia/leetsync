class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        s = s.rstrip()
        temp = s.split(" ")
        return(len(temp[-1]))