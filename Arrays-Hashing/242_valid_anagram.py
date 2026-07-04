# Easy - Arrays & Hashing

class Solution(object):
    def isAnagram(self, s, t):
        dict1={}
        dict2={}
        if len(s)!=len(t):
            return False
        else:
            for char in s:
                    dict1[char] =dict1.get(char,0)+1  # increment
            for char in t:
                    dict2[char] =dict2.get(char,0)+1  # increment
            return dict1==dict2

    
    

        
        