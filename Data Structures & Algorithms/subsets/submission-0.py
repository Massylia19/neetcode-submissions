class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_path = []  # Créé ici, accessible partout en bas
        
        def backtrack(index):
            if index == len(nums):
                result.append(list(current_path))
                return
            
            # Choix 1 : OUI
            current_path.append(nums[index])
            backtrack(index + 1)  # Plus besoin de passer current_path
            
            # Backtrack
            current_path.pop()
            
            # Choix 2 : NON
            backtrack(index + 1)
            
        backtrack(0)  # On appelle juste backtrack(0)
        return result

        