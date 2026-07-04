# Problem: Container With Most Water
# LeetCode: 11
# Difficulty: Medium
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            width=r-l
            max_area=max(max_area,width*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
                
          
        