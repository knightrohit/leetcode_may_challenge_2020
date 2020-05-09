"""
Input: 16
Output: true

Input: 14
Output: false
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == None:
            return False
        
        return (num**0.5).is_integer()