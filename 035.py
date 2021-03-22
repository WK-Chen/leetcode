class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low < high:
            if nums[mid] == target:
                return mid
            elif n