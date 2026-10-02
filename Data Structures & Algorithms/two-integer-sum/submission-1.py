class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i, num in enumerate(nums):
            missing = target - num
            if missing in dict:
                return [dict[missing], i]
            dict[num] = i
        return []
