# Problem: Maximum Number of Vowels in a Substring of Given Length
# LeetCode: 1456
# Difficulty: Medium
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels="aeiou"
        current_count = sum(1 for char in s[0:k] if char in vowels)
        max_count=current_count
        for i in range(k,len(s)):
            if s[i] in vowels:
                current_count+=1
            if s[i-k] in vowels:
                current_count-=1
            max_count=max(max_count,current_count)
        return max_count
                
        