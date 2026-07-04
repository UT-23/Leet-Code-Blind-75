# Problem: Contiguous Array
# LeetCode: 525
# Difficulty: Medium
# Topic: Arrays & Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        hashmap={0:-1}
        run_sum=0
        for i,num in enumerate(nums):
            run_sum += 1 if num == 1 else -1
            if run_sum in hashmap:
                count=max(count,i-hashmap[run_sum])
            else:
                hashmap[run_sum]=i
        return count

