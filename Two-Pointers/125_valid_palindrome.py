# Easy - Two Pointers

class Solution(object):
    def isPalindrome(self, s):
    
        m = "".join(char for char in s.lower() if char.isalnum())
        left = 0
        right = len(m) - 1
        
        while left < right:
            if m[left] != m[right]:
                return False
            left += 1
            right -= 1
        
        return True