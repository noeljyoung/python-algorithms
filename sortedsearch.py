from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid # index of the target value
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1

        if target > nums[mid]:
            return mid + 1
        else:
            return mid


sol = Solution()
numbers = [1,3]
target = 0

index = sol.searchInsert(numbers, target)
print(index)