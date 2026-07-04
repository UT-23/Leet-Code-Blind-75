# Medium - Arrays & Hashing

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap={0:1}
        run_sum=0
        count=0
        for num in nums:
            run_sum+=num
            if run_sum-k in hashmap:
               count+=hashmap[run_sum-k]
            hashmap[run_sum]=hashmap.get(run_sum,0)+1
        return count
                