# Problem: 3Sum
# LeetCode: 15
# Difficulty: Medium
# Topic: Two Pointers
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution(object):
    def threeSum(self, nums):
        s=[]
        nums.sort()
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    s.append([nums[i], nums[l], nums[r]])
                    l=l+1
                    r=r-1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total>0:
                    r=r-1
                elif total<0:
                    l=l+1
        return s