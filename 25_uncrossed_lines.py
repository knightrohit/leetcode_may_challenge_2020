'''
Time/Space complexity = O(N)
'''

from functools import lru_cache
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        @lru_cache(None)
        def lcd(i, j):
            
            if i >= len(A) or j >= len(B):
                return 0
        
            if A[i] == B[j]:
                return 1 + lcd(i+1, j+1)
            else:
                return max(lcd(i, j+1),  lcd(i+1, j))
            
        return lcd(0,0)