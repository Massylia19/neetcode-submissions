class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1 

        while start <= end: 
            medium = (start + end) // 2 

            if target == nums[medium]: 
                return medium 
            elif target < nums[medium]: 
                end = medium - 1
            else: 
                start = medium + 1 
        
        return start 