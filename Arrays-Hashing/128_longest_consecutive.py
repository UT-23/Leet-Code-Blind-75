# Problem: Longest Consecutive Sequence
# LeetCode: 128
# Difficulty: Medium
# Topic: Arrays & Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets=set(nums)
        longest=0
        for num in sets:
            if num-1 not in sets:
                current=1
                while num+current in sets:
                    current+=1
                longest=max(longest,current)
        return longest
