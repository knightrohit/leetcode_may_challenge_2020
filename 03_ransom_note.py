"""
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if not ransomNote and not magazine:
            return True
        
        if not ransomNote and magazine:
            return True
        
        if ransomNote and not magazine:
            return False        
        
        r_dict, m_dict = defaultdict(int), defaultdict(int)
        
        for i in ransomNote:
            r_dict[i] += 1
            
        for i in magazine:
            m_dict[i] += 1
            
        for i in ransomNote:
            val = m_dict.get(i)
            if val and val >= r_dict[i]:
                pass
            else:
                return False
            
        return True