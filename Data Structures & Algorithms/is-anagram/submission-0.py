class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict = {}
        for num in s:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        for num in t: 
            if num in dict:
                dict[num] -=1
            else:
                return False
        return max(dict.values()) == 0
        
        

            

