class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_arr = [1] * n
        suffix_arr = [1] * n

        prefix_acc = 1
        for i in range(n):
            prefix_arr[i] = prefix_acc
            prefix_acc *= nums[i]

        suffix_acc = 1 
        for i in range(n-1, -1, -1):
            suffix_arr[i] = suffix_acc
            suffix_acc *= nums[i]
        
        res = [1] * n 
        for i in range(n):
            res[i] = prefix_arr[i] * suffix_arr[i]
        return res
