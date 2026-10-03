class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        count = [0] * 26 
        for str in strs: 
            count = [0] * 26 
            for i in str: 
                index = ord(i) - ord("a")
                count[index] +=1 

            key = tuple(count)

            if key not in dict:
                dict[key] = []

            dict[key].append(str)

        return list(dict.values())



        