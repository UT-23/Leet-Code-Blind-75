# Problem: Move Zeroes
# LeetCode: 283
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[left]=nums[i]
                left+=1
        for i in range(left,len(nums)):
             nums[i]=0
        return nums

        
        