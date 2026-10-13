class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ind_dict = {}
        for index, num in enumerate(nums): 
            component = target - num

            if component in ind_dict: 
                return [ind_dict[component], index]
            
            ind_dict[num] = index 