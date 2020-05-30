'''
Time/Space complexity = O(V+E)
'''

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not numCourses:
            return True
        
        # 0 not visited
        # 1 visiting
        # 2 visited
        a_list = defaultdict(list)
        stack = []
        visited = [0]*numCourses
        
        for i, j in prerequisites:
            a_list[j].append(i)

        def dfs(i):
            if visited[i] == 2: return True
            
            if visited[i] == 1: return False
            
            #visiting
            visited[i] = 1
            
            for n in a_list[i]:
                if not dfs(n): return False
            
            #processed when reached leaf node
            visited[i] = 2
            return True
            
        
        for i in range(numCourses):
            if not dfs(i): return False
            
        return True