"""
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
Input: [3,2,3]
Output: 3

Solution  - time/space complexity - O(n) 
"""
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        
        count_element = defaultdict(int)
        out = []

        for i in nums:
            count_element[i] += 1
            
        for key, val in count_element.items():
            if val > (len(nums)/2):
                out.append(key)
                
        if len(out) == 1:
            return out[0]
        
        else:
            return out


# Using Counter
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if not nums:
            return None       
         
        out = []
        count_element = Counter(nums)
            
        for key, val in count_element.items():
            if val > (len(nums)/2):
                out.append(key)
                
        if len(out) == 1:
            return out[0]
        
        else:
            return out