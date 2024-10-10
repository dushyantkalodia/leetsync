class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(xor,map(ord,t+s)))