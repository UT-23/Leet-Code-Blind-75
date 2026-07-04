# Problem: Remove Duplicates from Sorted Array
# LeetCode: 26
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
               nums[left]=nums[i]
               left+=1
        return left