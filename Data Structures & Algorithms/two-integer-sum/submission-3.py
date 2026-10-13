class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dicti = {}

        for index, num in enumerate(nums): 
            component = target - num 

            if component in dicti: 
                return [dicti[component], index]
            
            dicti[num] = index
        
       