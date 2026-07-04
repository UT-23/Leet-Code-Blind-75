# Problem: Majority Element
# LeetCode: 169
# Difficulty: Easy
# Topic: Arrays & Hashing
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        champ=0
        count=0
        for x in nums:
            if (count==0):
                count+=1
                champ=x
            else:
                if (x==champ):
                    count+=1
                else:
                    count-=1
        return champ

        