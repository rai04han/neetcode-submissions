class Solution:
    def isPalindrome(self, s: str) -> bool:
        l  = 0
        x = "".join([i for i in s if i.isalnum()]).lower()
        r = len(x)-1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        
        return True