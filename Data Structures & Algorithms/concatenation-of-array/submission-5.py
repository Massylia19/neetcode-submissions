class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        tab= []
        for i in range(2): 
            for num in nums:
                tab.append(num) 
        return tab


        