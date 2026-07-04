# Problem: Contains Duplicate
# LeetCode: 217
# Difficulty: Easy
# Topic: Arrays & Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False
            
      
            
                
      

        
        