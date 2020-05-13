"""
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2.

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200.

Time and Space complexity = O(N)
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if not num:
            return None
        
        if len(num) == k:
            return '0'        
        
        stack = []
        
        for i in num:
            
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
                
            stack.append(i)            
            
        while k > 0:
            stack.pop()
            k -= 1
            
        out = int(''.join(stack))
        return ''.join(stack).lstrip('0') if out else '0'



# Second Approach
# Time limit exceeded
from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if not num:
            return None
        
        if len(num) == k:
            return '0'
        
        
        def generate(number):
            if len(number) == 1:
                return '0'

            for i in range(len(number)):
                second = '' if i == len(number) - 1 else number[i+1:]
                yield number[:i] + second
        
        queue = deque()
        queue.append(num)
        min_val = float('inf')
        
        while queue:
            val = queue.popleft()
            
            if k > 0:
                for number in generate(val):
                    min_val = min(min_val, int(number))
                    
                queue.append(str(min_val))
                k -=  1
            else:
                min_val = val
                break
                    
        return min_val