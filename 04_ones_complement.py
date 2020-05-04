"""
Input: 5
Output: 2

"""
class Solution:
    def findComplement(self, num: int) -> int:
        
        if num == None:
            return None
        
        bits = len('{:b}'.format(num))
        
        ones = (1 << bits) - 1
        
        return num ^ ones