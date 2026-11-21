class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1 
        res = []

        while left < right: 
            summ = numbers[left] + numbers[right]

            if summ == target: 
                res = [left + 1, right + 1] 
                return res
            elif summ > target: 
                right -= 1
            else: 
                left += 1 