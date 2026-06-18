class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        left=0
        right=0
        max_length=0 
        for right in range(0,len(s)):
            if s[right] in seen and seen[s[right]]>=left:
                left=seen[s[right]]+1
            seen[s[right]]=right
            max_length=max(max_length,right-left+1)
        return max_length
        