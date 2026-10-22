class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = 0
        for i, num in enumerate(nums):
            remain = target - num
            if (remain in nums) and (nums.index(remain) != i):
                first = i
                second = nums.index(remain)
                break
        return sorted([first, second])