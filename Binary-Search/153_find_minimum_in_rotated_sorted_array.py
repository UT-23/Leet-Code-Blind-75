# Problem: Find Minimum in Rotated Sorted Array
# LeetCode: 153
# Difficulty: Medium
# Topic: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]


        