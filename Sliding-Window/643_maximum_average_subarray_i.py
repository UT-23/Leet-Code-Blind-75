# Problem: Maximum Average Subarray I
# LeetCode: 643
# Difficulty: Easy
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        current_sum=sum(nums[0:k])
        max_sum=current_sum

        for i in range(k,len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            max_sum=max(max_sum,current_sum)
        return float(max_sum)/k
        