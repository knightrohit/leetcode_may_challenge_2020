# The isBadVersion API is already defined
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return None
        
        if n == 1:
            return n if isBadVersion(n) else None
        
        start = 1
        end = n
        mid = 0
        bad = float('inf')
        
        while start < end:            
            mid = (start+end)//2

            if isBadVersion(mid):
                end = mid
                bad = min(bad, mid)
                
            else:
                start = mid + 1            
         
        if start == end:
            if isBadVersion(start):
                return start
        return bad