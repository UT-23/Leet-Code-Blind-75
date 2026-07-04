# Problem: Minimum Window Substring
# LeetCode: 76
# Difficulty: Hard
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need={}
        for c in t: 
            need[c] = need.get(c, 0) + 1
        have={}
        formed=0
        required=len(need)
        result=""
        left=0
        for right in range(len(s)):
            have[s[right]]= have.get(s[right], 0) + 1
            if have[s[right]] == need.get(s[right], 0):
                formed += 1 
            while formed == required:
                if not result or (right - left + 1) < len(result):
                    result = s[left:right+1]
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        return result