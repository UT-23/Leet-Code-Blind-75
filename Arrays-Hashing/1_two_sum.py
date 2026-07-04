# Problem: Two Sum
# LeetCode: 1
# Difficulty: Easy
# Topic: Arrays & Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        dict1={}
        for i,n in enumerate(nums):
            s=target-n
            if s in dict1:
                return [dict1[s],i]
            dict1[n]=i

        