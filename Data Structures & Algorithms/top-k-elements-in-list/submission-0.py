class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums: 
            if num not in dict:
                dict[num] = 1
            else: 
                dict[num] += 1 
                #sort tri les clés et nom par valeur
        sorted_keys = sorted(dict, key=dict.get, reverse=True)
        return sorted_keys[:k]