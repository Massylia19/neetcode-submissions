class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1 

        while start <= end: 
            medium = (start + end) // 2 

            if nums[medium] == target: #check si target is medium
                return medium 

            if nums[start] <= nums[medium]: # check if left side sorted 
                if nums[start] <= target < nums[medium]: # target is that side yes or no ? 
                    end = medium - 1
                else: # if not, go right 
                    start = medium + 1
            else: # check if right side sorted 
                if nums[medium] < target <= nums[end]:
                    start = medium + 1
                else:
                    end = medium - 1
            
        return -1