class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)

        while start < end: 
            medium = (start + end) // 2 
            if target == nums[medium]:
                return medium
            if target < nums[medium]: 
                end = medium 
            else: 
                start = medium + 1 
                
        return -1
