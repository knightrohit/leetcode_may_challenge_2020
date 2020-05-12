"""
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Input: [3,3,7,7,10,11,11]
Output: 10

Time Complexity = O(log N)
Space Complexity = O(1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if not nums:
            return None

        start = 0
        end = len(nums) - 1

        def bs(start, end):  
            if start > end:
                return None
            if start == end:
                return nums[start]

            mid = (start + end) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    return bs(mid + 2, end)
                else:
                    return bs(start, mid)

            else:
                if nums[mid] == nums[mid - 1]:
                    return bs(mid + 1, end)
                else:
                    return bs(start, mid - 1)

        return bs(start, end)