class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        left=0
        max_frequency=0
        result=0
        
        for right in range(0,len(s)):
            count[s[right]]=count.get(s[right], 0) + 1
            max_frequency=max(max_frequency,count[s[right]])
            if (right - left + 1) - max_frequency > k:
                count[s[left]]-=1
                left+=1
            result = max(result, right - left + 1)
        return result
        
        