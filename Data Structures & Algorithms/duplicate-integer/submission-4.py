class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}
        for num in nums: 
            if num in dictt: 
                dictt[num] += 1  
            else: 
                dictt[num] = 1 
        print(dictt)
        for num in dictt.values(): 
            if num > 1:
                return True 
        
        return False 

