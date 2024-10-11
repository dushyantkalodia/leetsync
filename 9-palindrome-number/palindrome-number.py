class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        r = 0
        temp = x

        while x>0:
            r = (r*10)+(x%10)
            x//=10

        return r == temp

