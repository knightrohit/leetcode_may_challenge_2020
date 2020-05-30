'''
Time Complexity = O(NlogN)
Space Complexity = O(N)
'''

from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        out = []
        d_dict = defaultdict(list)
        for x, y in points:
            d = (x**2 + y**2)**0.5
            d_dict[d].append([x,y])
            
        for key in sorted(d_dict):
            out.extend(d_dict[key])
            if len(out) >= K:
                return out[:K]