class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1 
            while left < right:
                somme = nums[i] + nums[left] + nums[right]
                if somme < 0: 
                    left +=1 
                elif somme > 0: 
                        right -=1
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
        