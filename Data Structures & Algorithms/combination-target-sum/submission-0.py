class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def explorer(index_départ, reste, chemin): 
            if reste == 0: 
                return res.append(chemin.copy())

            if reste < 0: 
                return 
            
            for i in range(index_départ, len(nums)): 
                chemin.append(nums[i])

                explorer(i, reste - nums[i], chemin)
                chemin.pop()

        explorer(0, target, [])
        return res