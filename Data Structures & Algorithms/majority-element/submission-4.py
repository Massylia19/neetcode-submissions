class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}

        for num in nums: 
            if num in dict: 
                dict[num] += 1 
            else: 
                dict[num] = 1 

        best_value = 0 
        best_key = None

        for key in dict: 
            if dict[key] > best_value: 
                best_value = dict[key] #return value 
                best_key = key 
        
        return best_key 

        

        