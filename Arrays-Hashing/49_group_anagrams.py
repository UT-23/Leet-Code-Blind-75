# Problem: Group Anagrams
# LeetCode: 49
# Difficulty: Medium
# Topic: Arrays & Hashing
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap={}
        
        for word in strs:
            key=tuple(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key]=[word]
        return hashmap.values()

