"""
Find first unique character
s = "leetcode"
return 0

s = "loveleetcode",
return 2
"""

from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if not s:
            return -1
        
        ch_dict = OrderedDict()
        
        for indx, i in enumerate(s):
            if i in ch_dict:
                ch_dict[i].append(indx) 
            else:
                ch_dict[i] = [indx]
                
        for key, val in ch_dict.items():
            if len(val) == 1:
                return val[0]
        
        return -1