class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_index = {}
        for num in nums: 
            if num in dict_index: 
                dict_index[num] += 1
            else: 
                dict_index[num] = 1 

        sorted_elem = sorted(dict_index.keys(), key = dict_index.get, reverse = True)
        result = []
        
        for i in range(k):
            result.append(sorted_elem[i])

        return result 
        