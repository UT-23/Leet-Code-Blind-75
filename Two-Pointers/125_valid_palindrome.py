# Problem: Valid Palindrome
# LeetCode: 125
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

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