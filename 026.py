class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for quick in range(1, len(nums)):
            if nums[slow] != nums[quick]:
                slow += 1
                nums[slow] = nums[quick]
        return slow + 1