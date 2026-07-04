# Easy - Sliding Window

class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        count=0
        s=str(num)
        for left in range(len(s)-k+1):
            window=s[left:left+k]
            if int(window)!=0 and num%int(window)==0:
                count+=1
        return count


        