class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        left = 0 
        right = len(numbers) - 1 
        res = []

        while left < right: 
            sum = numbers[left] + numbers[right]

            if sum == target: 
                res = [left + 1, right + 1] 
                return res
            elif sum > target: 
                right -= 1
            else: 
                left += 1 