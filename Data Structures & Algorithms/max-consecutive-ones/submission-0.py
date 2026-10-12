class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i, num in enumerate(nums):
            if num == 1:
                count+=1
                if count > max_count:
                    max_count = count
            if num != 1:
                count = 0
        return max_count
        