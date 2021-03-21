class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for quick, _ in enumerate(nums):
            if nums[quick] == val:
                continue
            else:
                nums[slow] = nums[quick]
                slow = slow + 1
        return slow