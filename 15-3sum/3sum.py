        
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort the array
        res = []
        
        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # need bigger sum
                else:
                    right -= 1  # need smaller sum
        
        return res
