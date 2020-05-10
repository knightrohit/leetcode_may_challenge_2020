"""
Input: N = 2, trust = [[1,2]]
Output: 2

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Time complexity : O(N**2)
Space Complexity: O(N**2)
"""
from collections import defaultdict
def findJudge(N, trust):
    
        if not trust:
            return 1
        
        if not trust[0]:
            return -1
        
        if len(trust) == 1 and len(trust[0]) == 2:
            return trust[0][1]
         
        people = defaultdict(set)
        peoples = set()
        
        for i in trust:
            p, t = i
            people[p].add(t)
            peoples.add(p)
            peoples.add(t)
          
        out = peoples - people.keys()
        i = 0
        prev = 0
        for key, val in people.items():
            if i == 0:
                prev = val
            else:
                prev = prev.intersection(val)
            i += 1
                
        if prev == out and len(out) == 1:
            return out.pop()
        
        else:
            return -1

print(findJudge(2, [[1,2]]))