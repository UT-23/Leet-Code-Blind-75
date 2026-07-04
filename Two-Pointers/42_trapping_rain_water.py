# Problem: Trapping Rain Water
# LeetCode: 42
# Difficulty: Hard
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_water=0
        n=len(height)
        l,r=0,n-1
        left_max,right_max=0,0
        while l<r:
            if height[l]<height[r]:
                left_max=max(left_max,height[l])
                total_water+=left_max-height[l]
                l+=1
            else:
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
                r -= 1
        return total_water

        