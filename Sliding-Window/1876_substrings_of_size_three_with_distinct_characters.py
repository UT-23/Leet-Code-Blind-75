# Easy - Sliding Window

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count=0
        current_sum=sum(arr[0:k])
        if current_sum / k >= threshold:
            count += 1
        for i in range(k,len(arr)):
            current_sum=current_sum-arr[i-k]+arr[i]
            if (current_sum/k)>=threshold:
                count+=1
        return count
        