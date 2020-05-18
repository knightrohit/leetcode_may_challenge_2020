"""
Input: s1 = "ab" s2 = "eidbaooo"
Output: True

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Time Complexity = O(N)
Space Complexity = O(1)
"""

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if not s1 or not s2:
            return False
        
        if len(s1) > len(s2):
            return False
        
        hash1 = sum(hash(i) for i in s1)
        hash2 = sum(hash(i) for i in s2[:len(s1)])
        
        if hash1 == hash2:
            return True
        
        for out, in_ in zip(s2, s2[len(s1):]):
            hash2 += hash(in_) - hash(out)
            if hash1 == hash2:
                return True

        return False