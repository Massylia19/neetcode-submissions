class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start_pointer = 0 
        next_pointer = 1

        while next_pointer < len(nums): 
                if nums[start_pointer] != nums[next_pointer]: 
                    next_pointer += 1 
                    start_pointer += 1 

                else: 
                    nums.pop(next_pointer)

        return len(nums) 
