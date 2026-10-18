class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deja_vu = set()

        for num in nums: 
            if num in deja_vu: 
                return True
            deja_vu.add(num)

        return False