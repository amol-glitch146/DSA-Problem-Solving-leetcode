from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Update closest sum if found better
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
