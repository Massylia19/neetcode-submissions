class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1 

        while start < end: 
            medium = (start+end) // 2

            if nums[medium] > nums[end]: 
                start = medium + 1 
            else: 
                end = medium 

        return nums[start]
