from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        if not J:
            return None
        
        if not S:
            return 0
        
        stone_dict = defaultdict(int)
        count = 0
        
        for i in S:
            stone_dict[i] += 1
            
        for i in J:
            val = stone_dict.get(i)
            if val:
                count += val
                
        return count