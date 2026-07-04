
# Problem: Plus One
# LeetCode: 66
# Difficulty: Easy
# Topic: Arrays & Hashing
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
      
        n=len(digits)
        for n in range(n-1,-1,-1):
            if digits[n]!=9:
                digits[n]+=1
                break
            else:
                digits[n]=0
        if digits[0] == 0:
            digits = [1] + digits
        return digits
              