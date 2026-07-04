# Problem: Max Consecutive Ones III
# LeetCode: 1004
# Difficulty: Medium
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        result=0
        zero_count=0
        for right in range(0,len(nums)):
            if nums[right]==0:
                zero_count+=1
            if zero_count>k:
                if nums[left] == 0 :
                    zero_count-=1
                left+=1
            result=max(result,right-left+1)
        return result
        